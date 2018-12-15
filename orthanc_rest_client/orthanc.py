from apiron.service.base import Service
from apiron.endpoint import JsonEndpoint
from apiron.client import ServiceCaller
from urllib.parse import urlunparse

__all__=['Orthanc']


class OrthancService(Service):
    def __init__(self, *args, **kwargs):
        scheme = kwargs.pop('scheme', 'http')
        domain = kwargs.pop('domain', 'localhost')
        port = kwargs.pop('port', 8042)
        self.path = kwargs.pop('path', '')
        self.domain = urlunparse((scheme, ':'.join((domain, str(port))), self.path, '', '', ''))
        self._endpoints()
        super(*args, **kwargs)

    def _add_base_to_path(self, addition):
        return '/'.join((self.path.rstrip('/'), addition.lstrip('/'))) if self.path else addition

    def _endpoints(self):
        self.patients = JsonEndpoint(path=self._add_base_to_path('/patients'))
        self.patient = JsonEndpoint(path=self._add_base_to_path('/patients/{id}'))
        self.studies = JsonEndpoint(path=self._add_base_to_path('/studies'))
        self.study = JsonEndpoint(path=self._add_base_to_path('/studies/{id}'))
        self.series = JsonEndpoint(path=self._add_base_to_path('/series'))
        self.part = JsonEndpoint(path=self._add_base_to_path('/series/{id}'))
        self.instances = JsonEndpoint(path=self._add_base_to_path('/instances'))
        self.instance = JsonEndpoint(path=self._add_base_to_path('/instances/{id}'))
        self.instance_tag = JsonEndpoint(path=self._add_base_to_path('/instances/{id}/simplified-tags'))
        self.changes = JsonEndpoint(path=self._add_base_to_path('/changes'))
        self.queries = JsonEndpoint(path=self._add_base_to_path('/queries'))
        self.find = JsonEndpoint(path=self._add_base_to_path('/tools/find'), default_method='POST')
        self.shutdown = JsonEndpoint(path=self._add_base_to_path('tools/shutdown'), default_method='POST')

class Orthanc:
    """REST client for Orthanc REST endpoints

    :param scheme: http or https, default 'http'
    :type scheme: str
    :param domain: server domain (e.g., localhost, example.com/orthanc, etc), default 'localhost'
    :type domain: str
    :param port: port number, default 80
    :type port: int
    :param path: path (e.g., '/orthanc/rest'), default ''
    :type path: str

    .. NOTE: Can pass other keyword arguments through to <apiron.service.base.Service>

    """

    def __init__(self, *args, **kwargs):
        self.service = OrthancService(*args, **kwargs)

    @property
    def server(self):
        return self.service.domain

    def __repr__(self):
        return '<Orthanc server at {}>'.format(self.service.domain)

    def patients(self, id_=None, **kwargs):
        if id_:
            return ServiceCaller.call(self.service, self.service.patient, path_kwargs={'id': id_}, **kwargs)
        else:
            return ServiceCaller.call(self.service, self.service.patients, **kwargs)

    def studies(self, id_=None, **kwargs):
        if id_:
            return ServiceCaller.call(self.service, self.service.study, path_kwargs={'id': id_}, **kwargs)
        else:
            return ServiceCaller.call(self.service, self.service.studies, **kwargs)

    def series(self, id_=None, **kwargs):
        if id_:
            return ServiceCaller.call(self.service, self.service.part, path_kwargs={'id': id_}, **kwargs)
        else:
            return ServiceCaller.call(self.service, self.service.series, **kwargs)

    def instances(self, id_=None, **kwargs):
        if id_:
            return ServiceCaller.call(self.service, self.service.instance, path_kwargs={'id': id_}, **kwargs)
        else:
            return ServiceCaller.call(self.service, self.service.instances, **kwargs)

    def instance_tag(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.instance_tag, path_kwargs={'id': id_}, **kwargs)

    def changes(self, **kwargs):
        return ServiceCaller.call(self.service, self.service.changes, **kwargs)

    def queries(self, **kwargs):
        return ServiceCaller.call(self.service, self.service.queries, **kwargs)

    def find(self, query, **kwargs):
        '''Search for objects

        <query>: dict
            'Casesensitive'
            'Expand'
            'Level'
            'Limit'
            'Query'
            'Since'
        '''
        return ServiceCaller.call(self.service, self.service.find, data=query, **kwargs)

    def shutdown(self, **kwargs):
        return ServiceCaller.call(self.service, self.service.shutdown, **kwargs)


    ### Specific functions
    def get_patient_id_from_id(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.patient, path_kwargs={'id': id_}, **kwargs).get('MainDicomTags').get('PatientID')

    def get_all_studies_from_id(self, id_, **kwargs):
        return [self.studies(study, **kwargs) for study in self.patients(id_, **kwargs).get('Studies')]

    def get_all_studies_from_patient_id(self, id_, **kwargs):
        return [self.studies(study, **kwargs) for study in self.find({'Level': 'Study', 'Query': {'PatientID': id_}}, **kwargs)]

    def get_patients_with_name(self, search, **kwargs):
        return [self.patients(patient, **kwargs) for patient in self.find({'Level': 'Patient', 'CaseSensitive': False, 'Query': {'PatientName': search}})]
