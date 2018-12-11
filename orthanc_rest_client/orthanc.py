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
        self.domain = urlunparse((scheme, ':'.join((domain, str(port))), '', '', '', ''))
        super(*args, **kwargs)

    patients = JsonEndpoint(path='/patients')
    patient = JsonEndpoint(path='/patient/{id}')
    studies = JsonEndpoint(path='/studies')
    study = JsonEndpoint(path='/studies/{id}')
    series = JsonEndpoint(path='/series')
    part = JsonEndpoint(path='/series/{id}')
    instances = JsonEndpoint(path='/instances')
    instance = JsonEndpoint(path='/instances/{id}')
    instance_tag = JsonEndpoint(path='/instances/{id}/simplified-tags')
    changes = JsonEndpoint(path='/changes')
    queries = JsonEndpoint(path='/queries')
    find = JsonEndpoint(path='/tools/find', default_method='POST', required_params=['Level'])

class Orthanc:
    """Interface to apiron

    """

    def __init__(self, *args, **kwargs):
        self.service = OrthancService(*args, **kwargs)

    @property
    def server(self):
        return self.service.domain

    def __repr__(self):
        return '<Orthanc server at {}>'.format(self.service.domain)

    def patients(self):
        return ServiceCaller.call(self.service, self.service.patients)

    def patient(self, id_):
        return ServiceCaller.call(self.service, self.service.patient, path_kwargs={'id': id_})

    def studies(self):
        return ServiceCaller.call(self.service, self.service.studies)

    def study(self, id_):
        return ServiceCaller.call(self.service, self.service.study, path_kwargs={'id': id_})

    def series(self):
        return ServiceCaller.call(self.service, self.service.series)

    def part(self, id_):
        return ServiceCaller.call(self.service, self.service.part, path_kwargs={'id': id_})

    def instances(self):
        return ServiceCaller.call(self.service, self.service.instances)

    def instance(self, id_):
        return ServiceCaller.call(self.service, self.service.instance, path_kwargs={'id': id_})

    def instance_tag(self, id_):
        return ServiceCaller.call(self.service, self.service.instance_tag, path_kwargs={'id': id_})

    def changes(self):
        return ServiceCaller.call(self.service, self.service.changes)

    def queries(self):
        return ServiceCaller.call(self.service, self.service.queries)

    def find(self, level):
        return ServiceCaller.call(self.service, self.service.find, data={'Level': level})
