from apiron.service.base import Service
from apiron.endpoint import JsonEndpoint, StreamingEndpoint, Endpoint
from apiron.client import ServiceCaller

__all__=['Orthanc']

class OrthancService(Service):
    def __init__(self, domain, *args, **kwargs):
        self.domain = domain if domain.endswith('/') else '/'.join((domain, ''))
        super(*args, **kwargs)

    #### PATIENTS
    patients = JsonEndpoint(path='patients/')
    patient = JsonEndpoint(path='patients/{id}/')
    studies_of_patient = JsonEndpoint(path='patients/{id}/studies/')
    statistics_of_patient = JsonEndpoint(path='patients/{id}/statistics/')
    anonymize_patient = JsonEndpoint(path='patients/{id}/anonymize/')

    #### STUDIES
    studies = JsonEndpoint(path='studies/')
    study = JsonEndpoint(path='studies/{id}/')
    archive = StreamingEndpoint(path='studies/{id}/archive/')
    all_series_from_study = JsonEndpoint(path='studies/{id}/series/')
    patient_from_study = JsonEndpoint(path='studies/{id}/patient/')
    statistics_of_study = JsonEndpoint(path='studies/{id}/statistics/')
    anonymize_study = JsonEndpoint(path='studies/{id}/anonymize/')

    #### SERIES
    series = JsonEndpoint(path='series/')
    specific_series = JsonEndpoint(path='series/{id}/')
    statistics_of_series = JsonEndpoint(path='series/{id}/statistics/')
    anonymize_series = JsonEndpoint(path='series/{id}/anonymize/')

    #### INSTANCES
    instances = JsonEndpoint(path='instances/')
    instance = JsonEndpoint(path='instances/{id}/')
    instance_tag = JsonEndpoint(path='instances/{id}/simplified-tags/')
    statistics_of_instance = JsonEndpoint(path='instances/{id}/statistics/')
    anonymize_instance = JsonEndpoint(path='instances/{id}/anonymize/')

    #### OTHER
    statistics = JsonEndpoint(path='statistics/')
    changes = JsonEndpoint(path='changes/')
    queries = JsonEndpoint(path='queries/')
    find = JsonEndpoint(path='tools/find/', default_method='POST')

    #### SERVER-RELATED
    shutdown = JsonEndpoint(path='tools/shutdown/', default_method='POST')
    reset = JsonEndpoint(path='tools/reset/', default_method='POST')
    conformance = Endpoint(path='tools/dicom-conformance/')
    system = JsonEndpoint(path='system/')
    plugins = JsonEndpoint(path='plugins/')
    plugin_info = JsonEndpoint(path='plugins/{id}/')
    plugins_js = Endpoint(path='plugins/explorer.js/')

class Orthanc:
    """REST client for Orthanc REST endpoints

    :param domain: Full url of the Orthanc REST endpoint (e.g., https://example.com:8888/orthanc/rest)
    :type domain: str
    :return: Orthanc REST client
    :rtype: :class:`Orthanc`

    .. NOTE: Can pass other keyword arguments through to `apiron.service.base.Service`
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

    def archive(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.archive, path_kwargs={'id': id_}, **kwargs)

    def series(self, id_=None, **kwargs):
        if id_:
            return ServiceCaller.call(self.service, self.service.specific_series, path_kwargs={'id': id_}, **kwargs)
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

    def conformance(self, **kwargs):
        return ServiceCaller.call(self.service, self.service.conformance, **kwargs)

    def reset(self, **kwargs):
        return ServiceCaller.call(self.service, self.service.reset, **kwargs)

    def system(self, **kwargs):
        return ServiceCaller.call(self.service, self.service.system, **kwargs)

    def plugins(self, **kwargs):
        return ServiceCaller.call(self.service, self.service.plugins, **kwargs)

    def plugin_info(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.plugin_info, path_kwargs={'id': id_}, **kwargs)

    def plugins_js(self, **kwargs):
        return ServiceCaller.call(self.service, self.service.plugins_js, **kwargs)

    def statistics(self, endpoint=None, id_=None, **kwargs):
        router = {
                    'Patient': self.service.statistics_of_patient,
                    'Study': self.service.statistics_of_study,
                    'Series': self.service.statistics_of_series,
                    'Instance': self.service.statistics_of_instance
                }
        if endpoint in router and id_ is not None:
            return ServiceCaller.call(self.service, router[endpoint], path_kwargs={'id': id_}, **kwargs)
        else:
            return ServiceCaller.call(self.service, self.service.statistics, **kwargs)

    def anonymize(self, endpoint, id_, **kwargs):
        router = {
                    'Patient': self.service.anonymize_patient,
                    'Study': self.service.anonymize_study,
                    'Series': self.service.anonymize_series,
                    'Instance': self.service.anonymize_instance,
                }
        return ServiceCaller.call(self.service, router[endpoint], path_kwargs={'id': id_}, **kwargs)

    ### More specific functions
    def get_patient_id_from_id(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.patient, path_kwargs={'id': id_}, **kwargs).get('MainDicomTags').get('PatientID')

    def get_all_studies_from_patient_uuid(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.studies_of_patient, path_kwargs={'id': id_}, **kwargs)

    def get_all_studies_from_patient_id(self, id_, **kwargs):
        try:
            return [self.get_all_studies_from_patient_uuid(patient) for patient in self.find({'Level': 'Patient', 'Limit': 1, 'Query': {'ID': id_}}, **kwargs)][0]
        except:
            return []

    def get_patients_with_name(self, search, **kwargs):
        return [self.patients(patient, **kwargs) for patient in self.find({'Level': 'Patient', 'CaseSensitive': False, 'Query': {'PatientName': search}})]

    def get_all_series_from_study(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.all_series_from_study, path_kwargs={'id': id_}, **kwargs)

    def get_patient_from_study(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.patient_from_study, path_kwargs={'id': id_}, **kwargs)
