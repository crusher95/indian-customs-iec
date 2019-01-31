from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()


setup(name='indian-customs-iec-dhawanutkarsh',
      description='This package allows to verify import-export code with indian customs and fetch useful information linked with the same.',
      long_description=long_description,
      version='0.1.0',
      url='https://github.com/crusher95/indian-customs-iec',
      author='Utkarsh Dhawan',
      author_email='dhawanutkarsh@gmail.com',
      license='Apache2',
      classifiers=[
          'Intended Audience :: Developers',
          'License :: Apache Software License',
          'Programming Language :: Python :: 3'
      ],
      packages=find_packages(),
      install_requires=[
          'PyYAML>=3.11',
          'sh>=1.11'
      ]
)