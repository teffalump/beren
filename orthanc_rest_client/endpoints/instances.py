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

__all__ = ["OrthancInstances"]


class OrthancInstances(Service):

    instances = JsonEndpoint(path="instances/")
    add_instance = JsonEndpoint(path="instances/", default_method="POST")
    instance = JsonEndpoint(path="instances/{id}/")
    del_instance = JsonEndpoint(path="instances/{id}/", default_method="DELETE")
    anonymize = JsonEndpoint(path="instances/{id}/anonymize/", default_method="POST")
    content = JsonEndpoint(path="instances/{id}/content")
    content_raw_tag = JsonEndpoint(path="instances/{id}/content/{group}-{element}/")
    # instance_content_raw_seq = JsonEndpoint(path='instances/{id}/content/{group}-{element}/{index}/')
    export = JsonEndpoint(path="instances/{id}/export/", default_method="POST")
    file_ = StreamingEndpoint(path="instances/{id}/file/")
    frames = JsonEndpoint(path="instances/{id}/frames/")
    frame_int16 = StreamingEndpoint(path="instances/{id}/frames/{number}/image-int16/")
    frame_uint16 = StreamingEndpoint(path="instances/{id}/frames/{number}/image-int16/")
    frame_uint8 = StreamingEndpoint(path="instances/{id}/frames/{number}/image-int16/")
    frame_matlab = Endpoint(path="instances/{id}/frames/{number}/matlab/")
    frame_preview = StreamingEndpoint(path="instances/{id}/frames/{number}/preview/")
    frame_raw = StreamingEndpoint(path="instances/{id}/frames/{number}/raw/")
    frame_raw_gz = StreamingEndpoint(path="instances/{id}/frames/{number}/raw.gz/")
    header = JsonEndpoint(path="instances/{id}/header/")
    image_int16 = StreamingEndpoint(path="instances/{id}/image-int16/")
    image_uint16 = StreamingEndpoint(path="instances/{id}/image-uint16/")
    image_uint8 = StreamingEndpoint(path="instances/{id}/image-uint8/")
    matlab = Endpoint(path="instances/{id}/matlab/")
    modify = JsonEndpoint(path="instances/{id}/modify/", default_method="POST")
    module = JsonEndpoint(path="instances/{id}/module/")
    patient = JsonEndpoint(path="instances/{id}/patient/")
    pdf = StreamingEndpoint(path="instances/{id}/pdf/")
    preview = StreamingEndpoint(path="instances/{id}/preview/")
    reconstruct = JsonEndpoint(
        path="instances/{id}/reconstruct/", default_method="POST"
    )
    series = JsonEndpoint(path="instances/{id}/series/")
    simplified_tags = JsonEndpoint(path="instances/{id}/simplified-tags/")
    statistics = JsonEndpoint(path="instances/{id}/statistics/")
    study = JsonEndpoint(path="instances/{id}/study/")
    tags = JsonEndpoint(path="instances/{id}/tags/")
