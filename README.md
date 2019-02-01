![Made with Love in India](https://madewithlove.org.in/badge.svg) [![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

# Indian Customs IEC [pyiec]

This package allows to verify import-export code with indian customs and fetch useful information linked with the same. This works on the technology utilized in [exportify.in](https://exportify.in) using information extracted from DGFT(Directorate General of Foreign Trade) portal.

## Installation
```
pip install pyiec
```

## Utilization

```
>>>import pyiec

# Verification of iec number
>>>pyiec_object = pyiec.pyiec(iec_no='0301014175', first_three_chars='acc')
# Checks for the validity of iec status
>>>pyiec_object.verify_iec()
>>>False
>>>pyiec_object = pyiec(iec_no='0305008111', first_three_chars='nis')
>>>pyiec_object.verify_iec()
>>>True
>>>pyiec_object.fetch_info()
>>>{'banker_details': {'account_no': 'XXXXXXXX345',
                    'account_type': '1 CA',
                    'bank_name': 'STANDARD CHARTERED BANK'},
 'bin': {'ext': 'FT001', 'pan': 'AACCN0695D'},
 'branches': ['Branch Code:16 5TH FLOOR ORCHID BUSINESS PARK,SOH  NA ROAD '
              'SECTOR 48 GURGAON,HARYANA PIN-122004',
              'Branch Code:14 NRPDC , WAREHOUSE NO.B -2A,PATAUDI  -KULANA '
              'ROAD, MDR-132,  VILLAGE LUHARI,HARYANA  PIN-245205',
              'Branch Code:12 EQUINOX BUSINESS PARK TOWER 3 4TH FLR,LBS MARG, '
              'OFF BANDRA KURLA COMP KURLA WEST MUMBAI,MAHARASHTRA PIN-400070',
              'Branch Code:8 GRAND PALLADIUM,5TH FLR.,B WING,,1  75,CST '
              'ROAD,KALINA,SANTACRUZ EAST,  MUMBAI,MAHARASHTRA  PIN-400098',
              'Branch Code:6 TVS LOGISTICS SERVICES LTD.SING,CO  '
              'MPOUND,OPP.NAVNIT MOTORS,DAPODA RD BHIWANDI DIST '
              'THANE,MAHARASHTRA  PIN-421302',
              'Branch Code:2 PLOT 1A SIPCOT INDUL PARK,ORAGADAM   MATHUR POST  '
              'DIST-KANCHEEPURAM,TAMIL NADU  PIN-602105',
              'Branch Code:5 BLDG.NO.3 PART,124A,VALLAM A,SRIPE  '
              'RAMBUDUR,KANCHEEPURAM,  TAMILNADU,TAMIL NADU  PIN-602105',
              'Branch Code:15 SURVEY NO. 678 679 680 681 682 686  ,PART A '
              'ECHUR VILLAGE SRIPERUMBUDUR TK,TAMIL NADU PIN-602106',
              'Branch Code:10 INDOSPACE SKCL INDL.PARK,BULD.NO.1  '
              ',,PANRUTI,B,V.W.MAIN RD.  SRIPERUMBUDUR,TAMIL NADU  PIN-631604'],
 'date_of_establishment': '2005-02-07',
 'directors': ['HARDEEP SINGH BRAR GURMEL SINGH BRAR  HOUSE NO D-104 RIDGEWOOD '
               'ESTATE,DL  F PHASE-IV GALLARIA DLF-IV  FARRUKHNAGAR '
               'GURGAON,HARYANA  PIN-122009 Phone/Email:4437196978',
               'JEROME YVES MARIE SAIGOT THIERRY SAIGOT A9/2, 2ND FLOOR,VASANT '
               'VIHAR    DELHI,DELHI PIN-110057 Phone/Email:9176610283',
               'KOJI KAWAKITA  KIHACHIKAWAKITA  3-21-3, '
               'NAGATAKITA,MINAMI-KUYOKAHA  MA-SHI KANAGAWA NA  JAPAN,NA  '
               'PIN-0 Phone/Email:0000000000'],
 'email': 'sudharsan.ranganathan@rnaipl.com',
 'exporter_type': '5 Merchant/Manufacturer',
 'file_date': '22.01.2019',
 'file_number': '04/04/131/53050/AM19/',
 'iec': '0305008111',
 'iec_allotment_date': '03.05.2005',
 'iec_status': True,
 'nature_of_concern': 'Private Limited',
 'party_name_and_address': 'NISSAN MOTOR INDIA PVT. LTD. PLOT-1A,SIPCOT '
                           'INDL.PARK,ORAGADAM,  ,MATHUR POST,DIST-KANCHIPPURM '
                           ', TAMILNADU,TAMIL NADU  PIN-602105',
 'phone': '919176610283',
 'rcmc_details': [],
 'registered_area_pincode': '602105',
 'registered_state': 'Tamil Nadu',
 'registration_details': []}
```


Cheers!

