import json
import re

import requests
import hashlib

from bs4 import BeautifulSoup


class pyiec:
    def __init__(self, iec_no, first_three_chars):
        self.__response = requests.post("http://164.100.128.144:8100/dgft/IecPrint", data={'iec': iec_no, 'name': first_three_chars},timeout=5).text
        self.__error_message = ["4287293b7ae768abaff661ec64afda9946d5c740b909f30b1b5040d618769761",
                                "fd13a6927ae11ab69c72047ce3feb855e27d4aac8ec1c6cc5d42b88bae12a9ad",
                                "e2f901ca48cd500f578034dcdb67cd297d2efa69b14af563a68f9509af8660ce"]
        self.__soup = BeautifulSoup(self.__response)

    def verify_iec(self):
        if hashlib.sha256(self.__response.encode()).hexdigest() in self.__error_message:
            return False
        return False if self.__soup.find_all('tr')[9].find(text=re.compile("Valid IEC")) is None else True

    def fetch_info(self):
        result = {'iec': '', 'iec_allotment_date': '', 'file_number': '', 'file_date': '', 'party_name_and_address': '',
                  'phone': '', 'email': '', 'exporter_type': '', 'iec_status': False, 'date_of_establishment': '',
                  'bin': {}, 'nature_of_concern': '', 'banker_details': {}, 'directors': [], 'branches': [],
                  'registration_details': [], 'rcmc_details': []}
        index = 0
        for tr in self.__soup.find_all('tr'):
            if index == 1:
                result['iec'] = tr.text.replace('IEC:', '').strip()
            elif index == 2:
                result['iec_allotment_date'] = tr.text.replace('IEC Allotment Date:', '').strip()
            elif index == 3:
                result['file_number'] = tr.text.replace('File Number:', '').strip()
            elif index == 4:
                result['file_date'] = tr.text.replace('File Date:', '').strip()
            elif index == 5:
                for br in tr.find_all("br"):
                    br.replace_with("\n")
                address = tr.text.replace('Party Name and Address:', '').replace('  ', '').strip().split('\n')
                result['party_name_and_address'] = ' '.join(address)
                result['registered_area_pincode'] = address[-1].replace('PIN-', '').strip()
                postal_code_url = "http://postalpincode.in/api/pincode/" + result['registered_area_pincode']
                pin_request = requests.get(postal_code_url)
                pin_response = json.loads(pin_request.text)
                if 'PostOffice' in pin_response:
                    result['registered_state'] = pin_response['PostOffice'][0]['State']
            elif index == 6:
                result['phone'] = tr.text.replace('Phone No:', '').strip()
            elif index == 7:
                result['email'] = tr.text.replace('e_mail:', '').strip()
            elif index == 8:
                result['exporter_type'] = tr.text.replace('Exporter Type:', '').strip()
            elif index == 9:
                result['iec_status'] = False if tr.find(text=re.compile("Valid IEC")) is None else True
            elif index == 10:
                result['date_of_establishment'] = tr.text.replace('Date of Establishment:', '').strip()
            elif index == 11:
                result['bin']['pan'] = tr.text.replace('BIN (PAN+Extension):', '').strip().split(' ')[0].strip()
                result['bin']['ext'] = tr.text.replace('BIN (PAN+Extension):', '').strip().split(' ')[1].strip()
            elif index == 14:
                result['nature_of_concern'] = ' '.join(tr.text.replace('Nature Of Concern:', '').split(' ')[1:]).strip()
            elif index == 15:
                result['banker_details']['bank_name'] = tr.text.replace('Banker Detail', '').split(':')[
                    1].replace('A/C', '').replace('Type', '').strip()
                result['banker_details']['account_type'] = tr.text.replace('Banker Detail', '').strip().split(':')[
                    2].replace(
                    'A/C', '').replace('No', '').strip()
                result['banker_details']['account_no'] = tr.text.replace('Banker Detail', '').strip().split(':')[
                    3].replace(
                    'A/C', '').replace('No', '').strip()
            elif index > 15:
                for br in self.__soup.find_all("br"):
                    br.replace_with("\n")
                if tr.find(text=re.compile("Branch Code:")) is not None:
                    result['branches'].append(tr.text.replace('  ', '').replace('\n', ' ').strip()[2:])
                elif tr.find(text=re.compile("Registration")) is not None:
                    result['registration_details'].append(tr.text.replace('  ', '').replace('\n', ' ').strip()[2:])
                elif ' '.join(tr.text[2:])[0].isdigit():
                    result['rcmc_details'].append(tr.text.replace('  ', '').replace('\n', ' ').strip()[2:])
                else:
                    result['directors'].append(tr.text.replace('  ', '').replace('\n', ' ').strip()[2:])
            index += 1
        return result