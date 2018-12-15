from apiron.service.base import Service
from apiron.endpoint import JsonEndpoint
from apiron.client import ServiceCaller
from urllib.parse import urlparse

__all__=['Orthanc']


class OrthancService(Service):
    def __init__(self, domain, *args, **kwargs):
        self.domain = domain if domain.endswith('/') else '/'.join((domain, ''))
        super(*args, **kwargs)

    patients = JsonEndpoint(path='patients')
    patient = JsonEndpoint(path='patients/{id}')
    studies = JsonEndpoint(path='studies')
    study = JsonEndpoint(path='studies/{id}')
    series = JsonEndpoint(path='series')
    part = JsonEndpoint(path='series/{id}')
    instances = JsonEndpoint(path='instances')
    instance = JsonEndpoint(path='instances/{id}')
    instance_tag = JsonEndpoint(path='instances/{id}/simplified-tags')
    changes = JsonEndpoint(path='changes')
    queries = JsonEndpoint(path='queries')
    find = JsonEndpoint(path='tools/find', default_method='POST')
    shutdown = JsonEndpoint(path='tools/shutdown', default_method='POST')


class Orthanc:
    """REST client for Orthanc REST endpoints

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
