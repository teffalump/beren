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

__all__ = ["OrthancStudies"]


class OrthancStudies(Service):

    studies = JsonEndpoint(path="/studies/")
    study = JsonEndpoint(path="/studies/{id}/")
    del_study = JsonEndpoint(path="/studies/{id}/", default_method="DELETE")
    anonymize = JsonEndpoint(path="/studies/{id}/anonymize/", default_method="POST")
    archive = StreamingEndpoint(path="/studies/{id}/archive/")
    instances = JsonEndpoint(path="/studies/{id}/instances/")
    instances_tags = JsonEndpoint(path="/studies/{id}/instances-tags/")
    media = StreamingEndpoint(path="/studies/{id}/media/")
    modify = JsonEndpoint(path="/studies/{id}/modify/", default_method="POST")
    module = JsonEndpoint(path="/studies/{id}/module/")
    module_patient = JsonEndpoint(path="/studies/{id}/module_patient/")
    patient = JsonEndpoint(path="/studies/{id}/patient/")
    reconstruct = JsonEndpoint(path="/studies/{id}/reconstruct/", default_method="POST")
    series = JsonEndpoint(path="/studies/{id}/series/")
    shared_tags = JsonEndpoint(path="/studies/{id}/shared-tags/")
    statistics = JsonEndpoint(path="/studies/{id}/statistics/")
