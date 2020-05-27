# beren

[![Build Status](https://travis-ci.com/teffalump/beren.svg?branch=master)](https://travis-ci.com/teffalump/beren)
[![PyPI version](https://badge.fury.io/py/beren.svg)](https://badge.fury.io/py/beren)

`beren` provides a REST client for [Orthanc](https://www.orthanc-server.com), an open-source DICOM server.

Built using the excellent [apiron](https://github.com/ithaka/apiron) library.

### Install

Use pip:

    pip install beren

### How to use

Import the client and provide the server details

    from beren import Orthanc
    orthanc = Orthanc('https://example-orthanc-server.com')

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

### Advanced Configuration

#### Timeouts

Some servers are slow (and some methods can be slow). For example, asking for all instances from a server can cause a timeout before the server responds. To
modify the timeout settings, use `apiron`'s `Timeout` class:

    from apiron import Timeout
    t = Timeout(read_timeout=6, connection_timeout=1)   # Modify the timeout

    from beren import Orthanc
    orthanc = Orthanc('https://example-orthanc-server.com')
    orthanc.slow_endpoint(timeout_spec=t)               # Use new timeout

Increase the read timeout if the endpoint is slow. Increase the connection timeout for slow servers.

#### Disable Certificate Checks

To disable TLS certificate checking, use sessions:

    import requests
    session = requests.sessions.Session()       # New session
    session.verify = False                      # Disable certificate checking

    from beren import Orthanc
    orthanc = Orthanc('https://example-orthanc-server.com')
    orthanc.get_patients(session=session)       # Use session

#### Non-HTTPS endpoints

The client will warn when using HTTP endpoints. Medical data is particularly sensitive, consequently, strongly consider using HTTPS.

You can disable the warning using the `warn_insecure` argument:

    from beren import Orthanc
    orthanc = Orthanc('http://insecure.endpoint.com', warn_insecure=False)

### Examples

To save an instance file to the local directory:

    from beren import Orthanc
    orthanc = Orthanc('https://example-orthanc-server.com')

    with open('test_file.dcm', 'wb') as dcm:
        for chunk in orthanc.get_instance_file(<instance_id>):
            dcm.write(chunk)

To get an archive of a series (DCM files in a zip file):

    from beren import Orthanc
    orthanc = Orthanc('https://example-orthanc-server.com')

    with open('test.zip', 'wb') as z:
        for chunk in orthanc.get_series_archive(<instance_id>):
            z.write(chunk)

### Further help

- [apiron](https://github.com/ithaka/apiron)
- [Orthanc documentation](https://book.orthanc-server.com)
- [Orthanc OpenAPI](https://api.orthanc-server.com)
- [Orthanc REST API spreadsheet](https://docs.google.com/spreadsheets/d/1muKHMIb9Br-59wfaQbDeLzAfKYsoWfDSXSmyt6P4EM8/pubhtml#)
