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

__all__=['OrthancStudies']

class OrthancStudiesService(BaseService):

    studies = JsonEndpoint(path='studies/')
    study = JsonEndpoint(path='studies/{id}/')
    del_study = JsonEndpoint(path='studies/{id}/', default_method=['DELETE'])
    anonymize = JsonEndpoint(path='studies/{id}/anonymize/', default_method=['POST'])
    archive = StreamingEndpoint(path='studies/{id}/archive/')
    instances = JsonEndpoint(path='studies/{id}/instances/')
    instances_tags = JsonEndpoint(path='studies/{id}/instances-tags/')
    media = StreamingEndpoint(path='studies/{id}/media/')
    modify = JsonEndpoint(path='studies/{id}/modify/', default_method=['POST'])
    module = JsonEndpoint(path='studies/{id}/module/')
    module_patient = JsonEndpoint(path='studies/{id}/module_patient/')
    patient = JsonEndpoint(path='studies/{id}/patient/')
    reconstruct = JsonEndpoint(path='studies/{id}/reconstruct/', default_method=['POST'])
    series = JsonEndpoint(path='studies/{id}/series/')
    shared_tags = JsonEndpoint(path='studies/{id}/shared-tags/')
    statistics = JsonEndpoint(path='studies/{id}/statistics/')


class OrthancStudies(BaseCaller):
    def __init__(self, *args, **kwargs):
        self.service = OrthancStudiesService(*args, **kwargs)

    def get_studies(self, **kwargs):
        return ServiceCaller.call(self.service, self.service.studies, **kwargs)

    def get_study(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.sudy, path_kwargs={'id': id_}, **kwargs)

    def delete_study(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.del_study, path_kwargs={'id': id_}, **kwargs)

    def anonymize_study(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.anonymize, path_kwargs={'id': id_}, **kwargs)

    def get_study_archive(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.archive, path_kwargs={'id': id_}, **kwargs)

    def get_study_instances(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.instances, path_kwargs={'id': id_}, **kwargs)

    def get_study_instances_tags(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.instances_tags, path_kwargs={'id': id_}, **kwargs)

    def get_study_media(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.media, path_kwargs={'id': id_}, **kwargs)

    def modify_study(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.modify, path_kwargs={'id': id_}, **kwargs)

    def get_study_module(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.module, path_kwargs={'id': id_}, **kwargs)

    def get_study_module_patient(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.module_patient, path_kwargs={'id': id_}, **kwargs)

    def get_study_patient(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.patient, path_kwargs={'id': id_}, **kwargs)

    def reconstruct_study(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.reconstruct, path_kwargs={'id': id_}, **kwargs)

    def get_study_series(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.series, path_kwargs={'id': id_}, **kwargs)

    def get_study_shared_tags(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.shared_tags, path_kwargs={'id': id_}, **kwargs)

    def get_study_statistics(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.statistics, path_kwargs={'id': id_}, **kwargs)
