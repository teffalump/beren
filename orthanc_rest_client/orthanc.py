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

from orthanc_rest_client.endpoints import OrthancPatients, OrthancInstances, OrthancSeries

__all__=['Orthanc']

class Orthanc:
    def __init__(self, server, *args, **kwargs):
        self.patients = OrthancPatients(server, *args, **kwargs)
        self.instances = OrthancInstances(server, *args, **kwargs)
        self.series = OrthancSeries(server, *args, **kwargs)
