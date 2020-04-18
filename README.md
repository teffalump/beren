# beren

[![Build Status](https://travis-ci.com/teffalump/beren.svg?branch=master)](https://travis-ci.com/teffalump/beren)
[![PyPI version](https://badge.fury.io/py/beren.svg)](https://badge.fury.io/py/beren)

`beren` provides a REST client for [Orthanc](https://www.orthanc-server.com), an open-source DICOM server.

Built using the excellent [apiron](https://github.com/ithaka/apiron) library.

### Install

    pip install beren

### How to use

Import the client and provide the server details

    from beren import Orthanc
    orthanc = Orthanc('http://localhost:8042')

    # Patient endpoints
    orthanc.get_patients()
    orthanc.get_patient(id)
    ...and so on

    # Study endpoints
    orthanc.get_studies()
    orthanc.get_study(id)
    ...and so on

    # Series endpoints
    orthanc.get_series()
    orthanc.get_one_series(id)
    ...and so on

    # Instance endpoints
    orthanc.get_instances()
    orthanc.get_instance(id)
    ...and so on

    # Get changes
    orthanc.get_changes()

    # Find objects by query
    query = {'PatientName': 'Jon*'}
    orthanc.find(query, level='Patient', expand=False, limit=2)

    # Get previous queries
    orthanc.get_queries()

There are many other preconfigured endpoints.

### Authentication

Many servers require authentication to utilize their API. Simply provide a valid authentication object when defining the client:

    from requests.auth import HTTPBasicAuth
    auth = HTTPBasicAuth('orthanc', 'orthanc')
    orthanc = Orthanc('https://test.server.com', auth=auth)

### Advanced examples

For example, to save an instance file to the local directory:

    with open('test_file.dcm', 'wb') as dcm:
        for chunk in orthanc.get_instance_file(instance_id):
            dcm.write(chunk)

To get an archive of a series (DCM files in a zip file):

    with open('test.zip', 'wb') as z:
        for chunk in orthanc.get_series_archive(<id>):
            z.write(chunk)

### Security warning on non-HTTPS endpoints

The client will warn when using HTTP endpoints. Medical data is particularly sensitive, consequently, strongly consider using HTTPS.

You can disable the warning using the `warn_insecure` argument:

    orthanc = Orthanc('http://insecure.endpoint.com', warn_insecure=False)

### Further help

- [apiron](https://github.com/ithaka/apiron)
- [Orthanc documentation](https://book.orthanc-server.com)
- [Orthanc OpenAPI](https://api.orthanc-server.com)
- [Orthanc REST API spreadsheet](https://docs.google.com/spreadsheets/d/1muKHMIb9Br-59wfaQbDeLzAfKYsoWfDSXSmyt6P4EM8/pubhtml#)
