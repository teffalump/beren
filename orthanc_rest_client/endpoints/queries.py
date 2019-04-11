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

__all__ = ["OrthancQueries"]


class OrthancQueries(Service):

    queries = JsonEndpoint(path="queries/")
    query = JsonEndpoint(path="queries/{id}/")
    del_query = JsonEndpoint(path="queries/{id}/", default_method="DELETE")
    answers = JsonEndpoint(path="queries/{id}/answers/")
    answers_content = JsonEndpoint(path="queries/{id}/answers/{index}/content/")
    answers_retrieve = JsonEndpoint(
        path="queries/{id}/answers/{index}/retrieve/", default_method="POST"
    )
    level = JsonEndpoint(path="queries/{id}/level/")
    modality = JsonEndpoint(path="queries/{id}/modality/")
    query_query = JsonEndpoint(path="queries/{id}/query/")
    retrieve = JsonEndpoint(path="queries/{id}/retrieve/", default_method="POST")
