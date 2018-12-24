# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from apiron.service.base import Service
from apiron.endpoint import JsonEndpoint, StreamingEndpoint, Endpoint

__all__=['OrthancPatients']

class OrthancPatientsService(Service):
    def __init__(self, domain, *args, **kwargs):
        self.domain = domain if domain.endswith('/') else '/'.join((domain, ''))
        super(*args, **kwargs)

    patients= JsonEndpoint(path='patients/')
    patient = JsonEndpoint(path='patients/{id}/')
    anonymize = JsonEndpoint(path='patients/{id}/anonymize/', default_method='POST')
    archive = StreamingEndpoint(path='patients/{id}/archive/')
    instances = JsonEndpoint(path='patients/{id}/instances/')
    instances_tags = JsonEndpoint(path='patients/{id}/instances-tags/')
    modify = JsonEndpoint(path='patients/{id}/modify/', default_method=['POST'])
    module = JsonEndpoint(path='patients/{id}/module/')
    media = StreamingEndpoint(path='patients/{id}/media/')
    reconstruct = JsonEndpoint(path='patients/{id}/reconstruct/', default_method=['POST'])
    series = JsonEndpoint(path='patients/{id}/series/')
    shared_tags = JsonEndpoint(path='patients/{id}/shared-tags/')
    statistics = JsonEndpoint(path='patients/{id}/statistics/')
    studies = JsonEndpoint(path='patients/{id}/studies/')

class OrthancPatients:
    def __init__(self, *args, **kwargs):
        self.service = OrthancPatientsService(*args, **kwargs)

    def get_patients(self, **kwargs):
        return ServiceCaller.call(self.service, self.service.patients, **kwargs)

    def get_patient(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.patient, path_kwargs={'id': id_}, **kwargs)

    def anonymize_patient(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.anonymize, path_kwargs={'id': id_}, **kwargs)

    def archive_patient(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.archive, path_kwargs={'id': id_}, **kwargs)

    def get_patient_media(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.media, path_kwargs={'id': id_}, **kwargs)

    def get_patient_id_from_uuid(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.patient, path_kwargs={'id': id_}, **kwargs).get('MainDicomTags').get('PatientID')

    def get_studies_from_patient_uuid(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.studies, path_kwargs={'id': id_}, **kwargs)

    def get_instances_from_patient_uuid(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.instances, path_kwargs={'id': id_}, **kwargs)

    def get_series_from_patient_uuid(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.series, path_kwargs={'id': id_}, **kwargs)

    def get_patient_statistics(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.statistics, path_kwargs={'id': id_}, **kwargs)

    def get_all_studies_from_patient_id(self, id_, **kwargs):
        try:
            return [self.get_studies_from_patient_uuid(patient) for patient in self.find({'Level': 'Patient', 'Limit': 1, 'Query': {'PatientID': id_}}, **kwargs)][0]
        except:
            return []
