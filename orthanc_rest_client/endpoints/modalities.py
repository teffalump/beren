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

__all__ = ["OrthancModalities"]


class OrthancModalities(Service):

    modalities = JsonEndpoint("modalities/")
    modality = JsonEndpoint("modalities/{dicom}/")
    del_modality = JsonEndpoint("modalities/{dicom}/", default_method="DELETE")
    put_modality = JsonEndpoint("modalities/{dicom}/", default_method="PUT")
    echo = JsonEndpoint("modalities/{dicom}/echo/", default_method="POST")
    move = JsonEndpoint("modalities/{dicom}/move/", default_method="POST")
    query = JsonEndpoint("modalities/{dicom}/query/", default_method="POST")
    store = JsonEndpoint("modalities/{dicom}/store/", default_method="POST")
