# Beren

[![Build Status](https://travis-ci.com/teffalump/beren.svg?branch=master)](https://travis-ci.com/teffalump/beren)
[![PyPI version](https://badge.fury.io/py/beren.svg)](https://badge.fury.io/py/beren)

Provides a REST client targeted at [Orthanc](https://www.orthanc-server.com) REST API endpoints.

Based on the excellent [apiron](https://github.com/ithaka/apiron) library.

### Install

    pip install beren

### How to use

Import the pre-defined client and pass the server details

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

Pass valid auth object:

    from requests.auth import HTTPBasicAuth
    auth = HTTPBasicAuth('orthanc', 'orthanc')
    orthanc = Orthanc('https://test.server.com', auth=auth)

Then call functions normally (the auth object is passed automatically).

### Advanced examples

For example, to save an instance file to local directory:

    with open('test_file.dcm', 'wb') as dcm:
        for chunk in orthanc.get_instance_file(instance_id):
            dcm.write(chunk)

To get a zip of DCM files from a series:

    with open('test.zip', 'wb') as z:
        for chunk in orthanc.get_series_archive(<id>):
            z.write(chunk)

### Security warning on non-HTTPS endpoints

The rest client will warn when using HTTP endpoints. Strongly consider using HTTPS given the data sensitivity.

You can disable the warning using the `warn_insecure` keyword argument:

    orthanc = Orthanc('http://insecure.endpoint.com', warn_insecure=False)

### Further help

- [apiron](https://github.com/ithaka/apiron)
- [Orthanc documentation](https://book.orthanc-server.com)
- [Orthanc OpenAPI](https://api.orthanc-server.com)
- [Orthanc REST API spreadsheet](https://docs.google.com/spreadsheets/d/e/2PACX-1vSBEymDKGZgskFEFF6yzge5JovGHPK_FIbEnW5a6SWUbPkX06tkoObUHh6T1XQhgj-HqFd0AWSnVFOv/pubhtml?gid=654036639&single=true)
