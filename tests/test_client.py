from beren import Orthanc
from requests.auth import HTTPBasicAuth
from unittest import mock
import warnings
import pytest

URL = "https://demo.orthanc-server.com"
WEAK_URL = "http://demo.orthanc-server.com"
auth = HTTPBasicAuth("orthanc", "orthanc")
auth_bad = HTTPBasicAuth("bad", "bad")
orthanc = Orthanc(URL, auth=auth)


class TestClass:
    def test_server_target(self):
        assert orthanc._target == URL

    def test_server_auth(self):
        assert orthanc._auth.password == orthanc._auth.username == "orthanc"

    def test_domain_passing(self):
        assert orthanc.instances.domain == URL
        assert orthanc.series.domain == URL
        assert orthanc.studies.domain == URL
        assert orthanc.server.domain == URL
        assert orthanc.patients.domain == URL
        assert orthanc.queries.domain == URL
        assert orthanc.modalities.domain == URL

    def test_auth_passing(self):
        assert orthanc.instances.auth == auth
        assert orthanc.series.auth == auth
        assert orthanc.studies.auth == auth
        assert orthanc.server.auth == auth
        assert orthanc.patients.auth == auth
        assert orthanc.queries.auth == auth
        assert orthanc.modalities.auth == auth

    def test_connection_warning(self):
        with pytest.warns(UserWarning):
            Orthanc(WEAK_URL)

        with pytest.warns(None) as skip:
            Orthanc(WEAK_URL, warn_insecure=False)

        with pytest.warns(None) as record:
            Orthanc(URL)

        assert len(record) == 0
        assert len(skip) == 0
