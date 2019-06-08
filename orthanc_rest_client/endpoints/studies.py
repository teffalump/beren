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

from apiron import JsonEndpoint, StreamingEndpoint, Service

__all__ = ["OrthancStudies"]


class OrthancStudies(Service):

    studies = JsonEndpoint(path="/studies/")
    study = JsonEndpoint(path="/studies/{id}/")
    del_study = JsonEndpoint(path="/studies/{id}/", default_method="DELETE")
    anonymize = JsonEndpoint(path="/studies/{id}/anonymize/", default_method="POST")
    archive = StreamingEndpoint(path="/studies/{id}/archive/")
    attachments = JsonEndpoint(path="studies/{id}/attachments")
    attachment = JsonEndpoint(path="studies/{id}/attachment/{name}/")
    del_attachment = JsonEndpoint(
        path="studies/{id}/attachment/{name}/", default_method="DELETE"
    )
    put_attachment = JsonEndpoint(
        path="studies/{id}/attachment/{name}/", default_method="PUT"
    )
    compress_attachment = JsonEndpoint(
        path="studies/{id}/attachment/{name}/compress", default_method="POST"
    )
    compressed_attachment_data = JsonEndpoint(
        path="studies/{id}/attachment/{name}/compressed-data"
    )
    compressed_attachment_md5 = JsonEndpoint(
        path="studies/{id}/attachment/{name}/compressed-md5"
    )
    compressed_attachment_size = JsonEndpoint(
        path="studies/{id}/attachment/{name}/compressed-size"
    )
    attachment_data = JsonEndpoint(path="studies/{id}/attachment/{name}/data")
    attachment_is_compressed = JsonEndpoint(
        path="studies/{id}/attachment/{name}/is-compressed"
    )
    attachment_md5 = JsonEndpoint(path="studies/{id}/attachment/{name}/md5")
    attachment_size = JsonEndpoint(path="studies/{id}/attachment/{name}/size")
    uncompress_attachment = JsonEndpoint(
        path="studies/{id}/attachment/{name}/uncompress", default_method="POST"
    )
    verify_attachment = JsonEndpoint(
        path="studies/{id}/attachment/{name}/verify-md5", default_method="POST"
    )
    instances = JsonEndpoint(path="/studies/{id}/instances/")
    instances_tags = JsonEndpoint(path="/studies/{id}/instances-tags/")
    media = StreamingEndpoint(path="/studies/{id}/media/")
    list_metadata = JsonEndpoint(path="studies/{id}/metadata/")
    metadata = JsonEndpoint(path="studies/{id}/metadata/{name}/")
    del_metadata = JsonEndpoint(
        path="studies/{id}/metadata/{name}/", default_method="DELETE"
    )
    put_metadata = JsonEndpoint(
        path="studies/{id}/metadata/{name}/", default_method="PUT"
    )
    modify = JsonEndpoint(path="/studies/{id}/modify/", default_method="POST")
    module = JsonEndpoint(path="/studies/{id}/module/")
    module_patient = JsonEndpoint(path="/studies/{id}/module_patient/")
    patient = JsonEndpoint(path="/studies/{id}/patient/")
    reconstruct = JsonEndpoint(path="/studies/{id}/reconstruct/", default_method="POST")
    series = JsonEndpoint(path="/studies/{id}/series/")
    shared_tags = JsonEndpoint(path="/studies/{id}/shared-tags/")
    statistics = JsonEndpoint(path="/studies/{id}/statistics/")
