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
    patient = JsonEndpoint(path='/patients/{id}')
    studies = JsonEndpoint(path='/studies')
    study = JsonEndpoint(path='/studies/{id}')
    series = JsonEndpoint(path='/series')
    part = JsonEndpoint(path='/series/{id}')
    instances = JsonEndpoint(path='/instances')
    instance = JsonEndpoint(path='/instances/{id}')
    instance_tag = JsonEndpoint(path='/instances/{id}/simplified-tags')
    changes = JsonEndpoint(path='/changes')
    queries = JsonEndpoint(path='/queries')
    find = JsonEndpoint(path='/tools/find', default_method='POST')

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

    def patients(self, **kwargs):
        return ServiceCaller.call(self.service, self.service.patients, **kwargs)

    def patient(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.patient, path_kwargs={'id': id_}, **kwargs)

    def studies(self, **kwargs):
        return ServiceCaller.call(self.service, self.service.studies, **kwargs)

    def study(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.study, path_kwargs={'id': id_}, **kwargs)

    def series(self, **kwargs):
        return ServiceCaller.call(self.service, self.service.series, **kwargs)

    def part(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.part, path_kwargs={'id': id_}, **kwargs)

    def instances(self, **kwargs):
        return ServiceCaller.call(self.service, self.service.instances, **kwargs)

    def instance(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.instance, path_kwargs={'id': id_}, **kwargs)

    def instance_tag(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.instance_tag, path_kwargs={'id': id_}, **kwargs)

    def changes(self, **kwargs):
        return ServiceCaller.call(self.service, self.service.changes, **kwargs)

    def queries(self, ** kwargs):
        return ServiceCaller.call(self.service, self.service.queries, **kwargs)

    def find(self, query, **kwargs):
        return ServiceCaller.call(self.service, self.service.find, data=query, **kwargs)
