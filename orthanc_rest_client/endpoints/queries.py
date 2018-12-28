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

__all__=['OrthancQueries']

class OrthancQueriesService(BaseService):

    queries = JsonEndpoint(path='queries/')
    query = JsonEndpoint(path='queries/{id}/')
    del_query = JsonEndpoint(path='queries/{id}/', default_method=['DELETE'])
    answers = JsonEndpoint(path='queries/{id}/answers/')
    answers_content = JsonEndpoint(path='queries/{id}/answers/{index}/content/')
    answers_retrieve = JsonEndpoint(path='queries/{id}/answers/{index}/retrieve/', default_method=['POST'])
    level = JsonEndpoint(path='queries/{id}/level/')
    modality = JsonEndpoint(path='queries/{id}/modality/')
    query_query = JsonEndpoint(path='queries/{id}/query/')
    retrieve = JsonEndpoint(path='queries/{id}/retrieve/', default_method=['POST'])

class OrthancQueries(BaseCaller):
    def __init__(self, *args, **kwargs):
        self.service = OrthancQueriesService(*args, **kwargs)

    def get_queries(self, **kwargs):
        return ServiceCaller.call(self.service, self.service.queries, **kwargs)

    def get_query(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.query, path_kwargs={'id': id_}, **kwargs)

    def delete_query(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.del_query, path_kwargs={'id': id_}, **kwargs)

    def get_query_answers(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.query, path_kwargs={'id': id_}, **kwargs)

    def get_query_answers_content(self, id_, index, **kwargs):
        return ServiceCaller.call(self.service, self.service.answers_content, path_kwargs={'id': id_, 'index': index}, **kwargs)

    def post_query_answers_retrieve(self, id_, index, **kwargs):
        return ServiceCaller.call(self.service, self.service.answers_retrieve, path_kwargs={'id': id_, 'index': index}, **kwargs)

    def get_query_level(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.level, path_kwargs={'id': id_}, **kwargs)

    def get_query_modality(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.modality, path_kwargs={'id': id_}, **kwargs)

    def get_query_query(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.query_query, path_kwargs={'id': id_}, **kwargs)

    def post_query_retrieve(self, id_, **kwargs):
        return ServiceCaller.call(self.service, self.service.retrieve, path_kwargs={'id': id_}, **kwargs)
