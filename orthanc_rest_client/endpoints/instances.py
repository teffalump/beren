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

from .common import BaseService
from apiron.endpoint import JsonEndpoint, StreamingEndpoint, Endpoint

__all__=['OrthancInstancesService']

class OrthancInstancesService(BaseService):

    instances = JsonEndpoint(path='instances/')
    add_instance = JsonEndpoint(path='instances/', default_method=['POST'])
    instance = JsonEndpoint(path='instances/{id}/')
    del_instance = JsonEndpoint(path='instances/{id}/', default_method=['DELETE'])
    anonymize_instance = JsonEndpoint(path='instances/{id}/anonymize/', default_method=['POST'])
    instance_patient = JsonEndpoint(path='instances/{id}/patient/')
    statistics = JsonEndpoint(path='instances/{id}/statistics/')
    study = JsonEndpoint(path='instances/{id}/study/')
