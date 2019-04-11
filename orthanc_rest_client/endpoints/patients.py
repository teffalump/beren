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

from apiron import JsonEndpoint, StreamingEndpoint, Endpoint, Service

__all__ = ["OrthancPatients"]


class OrthancPatients(Service):

    patients = JsonEndpoint(path="patients/")
    patient = JsonEndpoint(path="patients/{id}/")
    del_patient = JsonEndpoint(path="patients/{id}/", default_method="DELETE")
    anonymize = JsonEndpoint(path="patients/{id}/anonymize/", default_method="POST")
    archive = StreamingEndpoint(path="patients/{id}/archive/")
    instances = JsonEndpoint(path="patients/{id}/instances/")
    instances_tags = JsonEndpoint(path="patients/{id}/instances-tags/")
    modify = JsonEndpoint(path="patients/{id}/modify/", default_method="POST")
    module = JsonEndpoint(path="patients/{id}/module/")
    media = StreamingEndpoint(path="patients/{id}/media/")
    protected = Endpoint(path="patients/{id}/protected/")
    put_protected = Endpoint(path="patients/{id}/protected/", default_method="PUT")
    reconstruct = JsonEndpoint(path="patients/{id}/reconstruct/", default_method="POST")
    series = JsonEndpoint(path="patients/{id}/series/")
    shared_tags = JsonEndpoint(path="patients/{id}/shared-tags/")
    statistics = JsonEndpoint(path="patients/{id}/statistics/")
    studies = JsonEndpoint(path="patients/{id}/studies/")
