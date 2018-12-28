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

__all__=['OrthancSeries']

class OrthancSeriesService(BaseService):

    series = JsonEndpoint(path='series/')
    part = JsonEndpoint(path='series/{id}/')
    del_part = JsonEndpoint(path='series/{id}/', default_method=['DELETE'])
    anonymize = JsonEndpoint(path='series/{id}/anonymize/', default_method=['POST'])
    archive = StreamingEndpoint(path='series/{id}/archive/')
    instances = JsonEndpoint(path='series/{id}/instances/')
    instances_tags = JsonEndpoint(path='series/{id}/instances-tags/')
    media = StreamingEndpoint(path='series/{id}/media/')
    modify = JsonEndpoint(path='series/{id}/modify/', default_method=['POST'])
    module = JsonEndpoint(path='series/{id}/module/')
    ordered_slices = JsonEndpoint(path='series/{id}/ordered-slices/')
    patient = JsonEndpoint(path='series/{id}/patient/')
    reconstruct = JsonEndpoint(path='series/{id}/reconstruct/', default_method=['POST'])
    shared_tags = JsonEndpoint(path='series/{id}/shared-tags/')
    statistics = JsonEndpoint(path='series/{id}/statistics/')
    study = JsonEndpoint(path='series/{id}/study/')


class OrthancSeries(BaseCaller):
    def __init__(self, *args, **kwargs):
        self.service = OrthancSeriesService(*args, **kwargs)

    def get_series(self, **kwargs):
        return ServiceCaller(self.service, self.service.series, **kwargs)

    def get_one_series(self, id_, **kwargs):
        return ServiceCaller(self.service, self.service.part, path_kwargs={'id': id_}, **kwargs)

    def delete_series(self, id_, **kwargs):
        return ServiceCaller(self.service, self.service.del_part, path_kwargs={'id': id_}, **kwargs)

    def anonymize_series(self, id_, **kwargs):
        return ServiceCaller(self.service, self.service.anonymize, path_kwargs={'id': id_}, **kwargs)

    def get_series_archive(self, id_, **kwargs):
        return ServiceCaller(self.service, self.service.archive, path_kwargs={'id': id_}, **kwargs)

    def get_series_instances(self, id_, **kwargs):
        return ServiceCaller(self.service, self.service.instances, path_kwargs={'id': id_}, **kwargs)

    def get_series_instances_tags(self, id_, **kwargs):
        return ServiceCaller(self.service, self.service.instances_tags, path_kwargs={'id': id_}, **kwargs)

    def get_series_media(self, id_, **kwargs):
        return ServiceCaller(self.service, self.service.media, path_kwargs={'id': id_}, **kwargs)

    def modify_series(self, id_, **kwargs):
        return ServiceCaller(self.service, self.service.modify, path_kwargs={'id': id_}, **kwargs)

    def get_series_module(self, id_, **kwargs):
        return ServiceCaller(self.service, self.service.module, path_kwargs={'id': id_}, **kwargs)

    def get_series_ordered_slices(self, id_, **kwargs):
        return ServiceCaller(self.service, self.service.ordered_slices, path_kwargs={'id': id_}, **kwargs)

    def get_series_patient(self, id_, **kwargs):
        return ServiceCaller(self.service, self.service.patient, path_kwargs={'id': id_}, **kwargs)

    def reconstruct_series(self, id_, **kwargs):
        return ServiceCaller(self.service, self.service.reconstruct, path_kwargs={'id': id_}, **kwargs)

    def get_series_shared_tags(self, id_, **kwargs):
        return ServiceCaller(self.service, self.service.shared_tags, path_kwargs={'id': id_}, **kwargs)

    def get_series_statistics(self, id_, **kwargs):
        return ServiceCaller(self.service, self.service.statistics, path_kwargs={'id': id_}, **kwargs)

    def get_series_study(self, id_, **kwargs):
        return ServiceCaller(self.service, self.service.study, path_kwargs={'id': id_}, **kwargs)
