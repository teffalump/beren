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

from .common import BaseService, BaseCaller
from apiron.endpoint import JsonEndpoint, StreamingEndpoint, Endpoint
from apiron.client import ServiceCaller

__all__=['OrthancPatients']

class OrthancPatientsService(BaseService):

    patients= JsonEndpoint(path='patients/')
    patient = JsonEndpoint(path='patients/{id}/')
    del_patient = JsonEndpoint(path='patients/{id}/', default_method=['DELETE'])
    anonymize = JsonEndpoint(path='patients/{id}/anonymize/', default_method='POST')
    archive = StreamingEndpoint(path='patients/{id}/archive/')
    instances = JsonEndpoint(path='patients/{id}/instances/')
    instances_tags = JsonEndpoint(path='patients/{id}/instances-tags/')
    modify = JsonEndpoint(path='patients/{id}/modify/', default_method=['POST'])
    module = JsonEndpoint(path='patients/{id}/module/')
    media = StreamingEndpoint(path='patients/{id}/media/')
    protected = Endpoint(path='patients/{id}/protected/')
    put_protected = Endpoint(path='patients/{id}/protected/', default_method=['PUT'])
    reconstruct = JsonEndpoint(path='patients/{id}/reconstruct/', default_method=['POST'])
    series = JsonEndpoint(path='patients/{id}/series/')
    shared_tags = JsonEndpoint(path='patients/{id}/shared-tags/')
    statistics = JsonEndpoint(path='patients/{id}/statistics/')
    studies = JsonEndpoint(path='patients/{id}/studies/')

class OrthancPatients(BaseCaller):
    def __init__(self, *args, **kwargs):
        self.service = OrthancPatientsService(*args, **kwargs)

    def get_patients(self, **kwargs):
        return ServiceCaller.call(self.service, self.service.patients, **kwargs)

    def get_patient(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.patient, path_kwargs={'id': id_}, **kwargs)

    def delete_patient(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.del_patient, path_kwargs={'id': id_}, **kwargs)

    def anonymize_patient(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.anonymize, path_kwargs={'id': id_}, **kwargs)

    def archive_patient(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.archive, path_kwargs={'id': id_}, **kwargs)

    def get_patient_instances(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.instances, path_kwargs={'id': id_}, **kwargs)

    def get_patient_instance_tags(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.instances_tags, path_kwargs={'id': id_}, **kwargs)

    def modify_patient(self, id_, data, **kwargs):
        return ServiceCaller.call(self.service, self.service.modify, path_kwargs={'id': id_}, data=data, **kwargs)

    def get_patient_module(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.module, path_kwargs={'id': id_}, **kwargs)

    def get_patient_media(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.media, path_kwargs={'id': id_}, **kwargs)

    def get_patient_protected(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.protected, path_kwargs={'id': id_}, **kwargs)

    def put_patient_protected(self, id_, data={}, **kwargs):
        return ServiceCaller.call(self.service, self.service.put_protected, path_kwargs={'id': id_}, data=data, **kwargs)

    def reconstruct_patient(self, id_, data={}, **kwargs):
        return ServiceCaller.call(self.service, self.service.protected, path_kwargs={'id': id_}, data=data, **kwargs)

    def get_patient_series(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.series, path_kwargs={'id': id_}, **kwargs)

    def get_patient_shared_tags(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.shared_tags, path_kwargs={'id': id_}, **kwargs)

    def get_patient_statistics(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.statistics, path_kwargs={'id': id_}, **kwargs)

    def get_patient_studies(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.studies, path_kwargs={'id': id_}, **kwargs)


    # UTILITY
    def get_patient_id_from_uuid(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.patient, path_kwargs={'id': id_}, **kwargs).get('MainDicomTags').get('PatientID')

    def get_patient_studies_from_id(self, id_, **kwargs):
        try:
            return [self.get_patient_studies(patient) for patient in self.find({'Level': 'Patient', 'Limit': 1, 'Query': {'PatientID': id_}}, **kwargs)][0]
        except:
            return []
