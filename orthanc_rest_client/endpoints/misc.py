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

__all__=['OrthancServerService']

class OrthancServerService(BaseService):

    changes = JsonEndpoint(path='changes/')
    del_changes = JsonEndpoint(path='changes/', default_method=['DELETE'])
    exports = JsonEndpoint(path='exports/')
    del_exports = JsonEndpoint(path='exports/', default_method=['DELETE'])

    jobs = JsonEndpoint(path='jobs/')
    job = JsonEndpoint(path='jobs/{id}/')
    cancel_job = JsonEndpoint(path='jobs/{id}/cancel/', default_method=['POST'])
    pause_job = JsonEndpoint(path='jobs/{id}/pause/', default_method=['POST'])
    resubmit_job = JsonEndpoint(path='jobs/{id}/resubmit/', default_method=['POST'])
    resume_job = JsonEndpoint(path='jobs/{id}/resume/', default_method=['POST'])

    peers = JsonEndpoint(path='peers/')
    peer = JsonEndpoint(path='peers/{peer}/')
    del_peer = JsonEndpoint(path='peers/{peer}/', default_method=['DELETE'])
    put_peer = JsonEndpoint(path='peers/{peer}/', default_method=['PUT'])
    store_peer = JsonEndpoint(path='peers/{peer}/store/', default_method=['POST'])

    plugins = JsonEndpoint(path='plugins/')
    plugin = JsonEndpoint(path='plugins/{id}/')
    plugins_js = Endpoint(path='plugins/explorer.js/')

    statistics = JsonEndpoint(path='statistics/')
    system = JsonEndpoint(path='system/')

    tools_create_archive = StreamingEndpoint(path='tools/create-archive/', default_method=['POST'])
    tools_create_dicom = StreamingEndpoint(path='tools/create-dicom/', default_method=['POST'])
    tools_create_media = StreamingEndpoint(path='tools/create-media/', default_method=['POST'])
    tools_create_media_extended = StreamingEndpoint(path='tools/create-media-extended/', default_method=['POST'])
    tools_default_encoding = JsonEndpoint(path='tools/default-encoding/')
    tools_post_default_encoding = JsonEndpoint(path='tools/default-encoding/', default_method=['POST'])
    tools_dicom_conformance = Endpoint(path='tools/dicom-conformance/')
    tools_execute_script = JsonEndpoint(path='tools/execute-script/', default_method=['POST'])
    tools_find = JsonEndpoint(path='tools/find/', default_method=['POST'])
    tools_generate_uid = JsonEndpoint(path='tools/generate-uid/')
    tools_invalidate_tags = JsonEndpoint(path='tools/invalidate-tags/', default_method=['POST'])
    tools_lookup = JsonEndpoint(path='tools/lookup/', default_method=['POST'])
    tools_now = Endpoint(path='tools/now/')
    tools_now_local = Endpoint(path='tools/now-local/')
    tools_reset = JsonEndpoint(path='tools/reset/', default_method=['POST'])
    tools_shutdown = JsonEndpoint(path='tools/shutdown/', default_method=['POST'])