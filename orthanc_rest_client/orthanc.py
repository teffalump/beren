from orthanc_rest_client.endpoints import OrthancPatients

__all__=['Orthanc']

class Orthanc:
    def __init__(self, domain, *args, **kwargs):
        self.patients = OrthancPatients(domain, *args, **kwargs)
