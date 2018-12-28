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

__all__=['OrthancInstances']

class OrthancInstancesService(BaseService):

    instances = JsonEndpoint(path='instances/')
    add_instance = JsonEndpoint(path='instances/', default_method=['POST'])
    instance = JsonEndpoint(path='instances/{id}/')
    del_instance = JsonEndpoint(path='instances/{id}/', default_method=['DELETE'])
    anonymize_instance = JsonEndpoint(path='instances/{id}/anonymize/', default_method=['POST'])
    instance_patient = JsonEndpoint(path='instances/{id}/patient/')
    statistics = JsonEndpoint(path='instances/{id}/statistics/')
    study = JsonEndpoint(path='instances/{id}/study/')


class OrthancInstances(BaseCaller):
    def __init__(self, *args, **kwargs):
        self.service = OrthancInstancesService(*args, **kwargs)

    def get_instances(self, **kwargs):
        return ServiceCaller.call(self.service, self.service.instances, **kwargs)

    def add_instance(self, dicom, **kwargs):
        return ServiceCaller.call(self.service, self.service.add_instance, data=dicom, **kwargs)

    def get_instance(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.instance, path_kwargs={'id': id_}, **kwargs)

    def delete_instance(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.del_instance, path_kwargs={'id': id_}, **kwargs)

    def anonymize_instance(self, id_, data={}, **kwargs):
        return ServiceCaller.call(self.service, self.service.del_instance, path_kwargs={'id': id_}, data=data, **kwargs)

    def get_instance_patient(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.instance_patient, path_kwargs={'id': id_}, **kwargs)

    def get_instance_statistics(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.statistics, path_kwargs={'id': id_}, **kwargs)

    def get_instance_study(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.study, path_kwargs={'id': id_}, **kwargs)
