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
    orthanc.find(query)

    # Get previous queries
    orthanc.get_queries()

There are other preconfigured endpoints.

### Authenticated Endpoints

Pass valid auth object:

    from requests.auth import HTTPBasicAuth
    auth = HTTPBasicAuth('orthanc', 'orthanc')
    orthanc = Orthanc('https://test.server.com', auth=auth)

Then call functions normally (the auth object is passed automatically).

For further help:
- [apiron](https://github.com/ithaka/apiron)
- [Orthanc documentation](http://book.orthanc-server.com) and [Orthanc REST API](https://docs.google.com/spreadsheets/d/e/2PACX-1vSBEymDKGZgskFEFF6yzge5JovGHPK_FIbEnW5a6SWUbPkX06tkoObUHh6T1XQhgj-HqFd0AWSnVFOv/pubhtml?gid=1094535210&single=true)
