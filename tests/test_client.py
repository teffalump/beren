from orthanc_rest_client import Orthanc


URL = 'http://demo.orthanc-server.com'

def test_server_target():
    orthanc = Orthanc(URL)
    assert orthanc._target == URL
