# Orthanc REST client

Provides a REST client targeted at [Orthanc](https://www.orthanc-server.com) REST API endpoints.

Based on the excellent [apiron](https://github.com/ithaka/apiron) library.

### Install

    pip install orthanc-rest-client

### How to use

Import the pre-defined client and pass the server details

    from orthanc_rest_client import Orthanc
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
    orthanc.get_studies()
    orthanc.get_study()
    ...and so on

    # Instances endpoints
    orthanc.get_instances()
    orthanc.get_instance(id)
    ...and so on

    # Get changes
    orthanc.changes()

    # Find objects by query
    orthanc.find(query)

    # Get previous queries
    orthanc.queries()

There are other preconfigured endpoints.

### Authenticated Endpoints

Pass valid Request auth objects:

    from requests.auth import HTTPBasicAuth
    orthanc.reset(auth=HTTPBasicAuth('orthanc', 'orthanc'))

For further help:
- [apiron](https://github.com/ithaka/apiron)
- [Orthanc documentation](http://book.orthanc-server.com) and [Orthanc REST API](https://docs.google.com/spreadsheets/d/e/2PACX-1vSBEymDKGZgskFEFF6yzge5JovGHPK_FIbEnW5a6SWUbPkX06tkoObUHh6T1XQhgj-HqFd0AWSnVFOv/pubhtml?gid=1094535210&single=true)
