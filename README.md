# Orthanc REST client

Provides a REST client, based on [apiron](https://github.com/ithaka/apiron), targeted at [Orthanc](https://www.orthanc-server.com) REST endpoints.

### Install

    pip install orthanc-rest-client

### How to use

Import the pre-defined client and pass the server details

    from orthanc_rest_client import Orthanc
    orthanc = Orthanc('http://localhost:8042')

    # Get patient(s)
    orthanc.patients(<id or not>)

    # Get studies/study
    orthanc.studies(<id or not>)

    # Get series/part
    orthanc.series(<id or not>)

    # Get instances/instance
    orthanc.instances(<id or not>)

    # Get tags
    orthanc.instance_tag(id)

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
- [Orthanc documentation](http://book.orthanc-server.com)
