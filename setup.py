import os
from setuptools import setup

NAME = 'beren'

with open('README.md') as readme:
    README = readme.read()
    README_TYPE = "text/markdown"

with open(os.path.join(NAME, 'VERSION')) as version:
    VERSION = version.readlines()[0].strip()

with open('requirements.txt') as requirements:
    REQUIREMENTS = [line.rstrip() for line in requirements if line != '\n']

setup(name = NAME,
        version = VERSION,
        description = 'REST client for Orthanc DICOM servers',
        long_description = README,
        long_description_content_type = README_TYPE,
        url = 'https://github.com/teffalump/beren',
        author = 'teffalump',
        author_email = 'chris@teffalump.com',
        packages = ['beren'],
        install_requires = REQUIREMENTS,
        include_package_data = True,
        zip_safe = False,
        classifiers = ['Development Status :: 4 - Beta',
                       'Programming Language :: Python :: 3',
                       'Programming Language :: Python :: 3 :: Only',
                       'Intended Audience :: Developers',
                       'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
                       'Operating System :: OS Independent'],
)
