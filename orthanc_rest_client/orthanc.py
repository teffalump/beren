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

from .endpoints import (
    OrthancInstances,
    OrthancModalities,
    OrthancPatients,
    OrthancQueries,
    OrthancSeries,
    OrthancServer,
    OrthancStudies,
)
from apiron.client import ServiceCaller
from json import dumps
from functools import partial

__all__ = ["Orthanc"]

# Authentication wrapper
def auth(function):
    def wrap(self, *args, **kwargs):
        if not kwargs.get("auth"):
            kwargs["auth"] = self._auth
        return function(self, *args, **kwargs)

    return wrap


class Orthanc:
    def __init__(self, server, auth=None):
        self._target = server
        self._auth = auth
        self.instances = OrthancInstances
        self.modalities = OrthancModalities
        self.patients = OrthancPatients
        self.queries = OrthancQueries
        self.series = OrthancSeries
        self.server = OrthancServer
        self.studies = OrthancStudies
        self.instances.domain = (
            self.modalities.domain
        ) = (
            self.patients.domain
        ) = (
            self.queries.domain
        ) = self.series.domain = self.server.domain = self.studies.domain = self._target

    def __repr__(self):
        return "<Orthanc REST client({})>".format(self._target)

    @staticmethod
    def convert_to_json(data, **kwargs):
        return dumps(data, **kwargs)

    #### INSTANCES
    @auth
    def get_instances(self, **kwargs):
        return self.instances.instances(**kwargs)

    @auth
    def add_instance(self, dicom, **kwargs):
        return self.instances.add_instance(data=dicom, **kwargs)

    @auth
    def get_instance(self, id_, **kwargs):
        return self.instances.instance(path_kwargs={"id": id_}, **kwargs)

    @auth
    def delete_instance(self, id_, **kwargs):
        return self.instances.del_instance(path_kwargs={"id": id_}, **kwargs)

    @auth
    def anonymize_instance(self, id_, data={}, **kwargs):
        j = self.convert_to_json(data)
        return self.instances.anonymize(path_kwargs={"id": id_}, data=j, **kwargs)

    @auth
    def get_instance_content(self, id_, **kwargs):
        return self.instances.content(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_instance_content_raw_tag(self, id_, **kwargs):
        return self.instances.content_raw_tag(path_kwargs={"id": id_}, **kwargs)

    @auth
    def export_instance(self, id_, **kwargs):
        return self.instances.export(path_kwargs={"id": id_}, data={}, **kwargs)

    @auth
    def get_instance_file(self, id_, **kwargs):
        return self.instances.file_(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_instance_frames(self, id_, **kwargs):
        return self.instances.frames(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_instance_frame_int16(self, id_, frame, **kwargs):
        return self.instances.frame_int16(
            path_kwargs={"id": id_, "number": frame}, **kwargs
        )

    @auth
    def get_instance_frame_uint16(self, id_, frame, **kwargs):
        return self.instances.frame_uint16(
            path_kwargs={"id": id_, "number": frame}, **kwargs
        )

    @auth
    def get_instance_frame_uint8(self, id_, frame, **kwargs):
        return self.instances.frame_uint8(
            path_kwargs={"id": id_, "number": frame}, **kwargs
        )

    @auth
    def get_instance_frame_matlab(self, id_, frame, **kwargs):
        return self.instances.frame_matlab(
            path_kwargs={"id": id_, "number": frame}, **kwargs
        )

    @auth
    def get_instance_frame_preview(self, id_, frame, **kwargs):
        return self.instances.frame_preview(
            path_kwargs={"id": id_, "number": frame}, **kwargs
        )

    @auth
    def get_instance_frame_raw(self, id_, frame, **kwargs):
        return self.instances.frame_raw(
            path_kwargs={"id": id_, "number": frame}, **kwargs
        )

    @auth
    def get_instance_frame_raw_gz(self, id_, frame, **kwargs):
        return self.instances.frame_raw_gz(
            path_kwargs={"id": id_, "number": frame}, **kwargs
        )

    @auth
    def get_instance_header(self, id_, **kwargs):
        return self.instances.header(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_instance_int16(self, id_, **kwargs):
        return self.instances.image_int16(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_instance_uint16(self, id_, **kwargs):
        return self.instances.image_uint16(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_instance_uint8(self, id_, **kwargs):
        return self.instances.image_uint8(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_instance_matlab(self, id_, **kwargs):
        return self.instances.matlab(path_kwargs={"id": id_}, **kwargs)

    @auth
    def modify_instance(self, id_, data, **kwargs):
        j = self.convert_to_json(data)
        return self.instances.modify(path_kwargs={"id": id_}, data=j, **kwargs)

    @auth
    def get_instance_module(self, id_, **kwargs):
        return self.instances.module(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_instance_patient(self, id_, **kwargs):
        return self.instances.patient(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_instance_pdf(self, id_, **kwargs):
        return self.instances.pdf(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_instance_preview(self, id_, **kwargs):
        return self.instances.preview(path_kwargs={"id": id_}, **kwargs)

    @auth
    def reconstruct_instance(self, id_, **kwargs):
        return self.instances.reconstruct(path_kwargs={"id": id_}, data={}, **kwargs)

    @auth
    def get_instance_series(self, id_, **kwargs):
        return self.instances.series(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_instance_simplified_tags(self, id_, **kwargs):
        return self.instances.simplified_tags(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_instance_statistics(self, id_, **kwargs):
        return self.instances.statistics(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_instance_study(self, id_, **kwargs):
        return self.instances.study(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_instance_tags(self, id_, **kwargs):
        return self.instances.tags(path_kwargs={"id": id_}, **kwargs)

    #### PATIENTS
    @auth
    def get_patients(self, **kwargs):
        return self.patients.patients(**kwargs)

    @auth
    def get_patient(self, id_, **kwargs):
        return self.patients.patient(path_kwargs={"id": id_}, **kwargs)

    @auth
    def delete_patient(self, id_, **kwargs):
        return self.patients.del_patient(path_kwargs={"id": id_}, **kwargs)

    @auth
    def anonymize_patient(self, id_, data={}, **kwargs):
        j = self.convert_to_json(data)
        return self.patients.anonymize(path_kwargs={"id": id_}, data=j, **kwargs)

    @auth
    def archive_patient(self, id_, **kwargs):
        return self.patients.archive(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_patient_instances(self, id_, **kwargs):
        return self.patients.instances(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_patient_instance_tags(self, id_, **kwargs):
        return self.patients.instances_tags(path_kwargs={"id": id_}, **kwargs)

    @auth
    def modify_patient(self, id_, data, **kwargs):
        j = self.convert_to_json(data)
        return self.patients(
            self._patients.modify, path_kwargs={"id": id_}, data=j, **kwargs
        )

    @auth
    def get_patient_module(self, id_, **kwargs):
        return self.patients.module(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_patient_media(self, id_, **kwargs):
        return self.patients.media(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_patient_protected(self, id_, **kwargs):
        return self.patients.protected(path_kwargs={"id": id_}, **kwargs)

    @auth
    def put_patient_protected(self, id_, data={}, **kwargs):
        return self.patients.put_protected(path_kwargs={"id": id_}, data=data, **kwargs)

    @auth
    def reconstruct_patient(self, id_, data={}, **kwargs):
        return self.patients.protected(path_kwargs={"id": id_}, data=data, **kwargs)

    @auth
    def get_patient_series(self, id_, **kwargs):
        return self.patients.series(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_patient_shared_tags(self, id_, **kwargs):
        return self.patients.shared_tags(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_patient_statistics(self, id_, **kwargs):
        return self.patients.statistics(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_patient_studies(self, id_, **kwargs):
        return self.patients.studies(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_patient_id_from_uuid(self, id_, **kwargs):
        return (
            self.patients.patient(path_kwargs={"id": id_}, **kwargs)
            .get("MainDicomTags")
            .get("PatientID")
        )

    @auth
    def get_patient_studies_from_id(self, id_, **kwargs):
        try:
            return [
                self.get_patient_studies(patient)
                for patient in self.find(
                    {"Level": "Patient", "Limit": 1, "Query": {"PatientID": id_}},
                    **kwargs
                )
            ][0]
        except:
            return []

    #### QUERIES
    @auth
    def get_queries(self, **kwargs):
        return self.queries.queries(**kwargs)

    @auth
    def get_query(self, id_, **kwargs):
        return self.queries.query(path_kwargs={"id": id_}, **kwargs)

    @auth
    def delete_query(self, id_, **kwargs):
        return self.queries.del_query(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_query_answers(self, id_, **kwargs):
        return self.queries.query(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_query_answers_content(self, id_, index, **kwargs):
        return self.queries.answers_content(
            path_kwargs={"id": id_, "index": index}, **kwargs
        )

    @auth
    def post_query_answers_retrieve(self, id_, index, **kwargs):
        return self.queries.answers_retrieve(
            path_kwargs={"id": id_, "index": index}, **kwargs
        )

    @auth
    def get_query_level(self, id_, **kwargs):
        return self.queries.level(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_query_modality(self, id_, **kwargs):
        return self.queries.modality(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_query_query(self, id_, **kwargs):
        return self.queries.query_query(path_kwargs={"id": id_}, **kwargs)

    @auth
    def post_query_retrieve(self, id_, **kwargs):
        return self.queries.retrieve(path_kwargs={"id": id_}, **kwargs)

    #### SERIES
    @auth
    def get_series(self, **kwargs):
        return self.series.series(**kwargs)

    @auth
    def get_one_series(self, id_, **kwargs):
        return self.series.part(path_kwargs={"id": id_}, **kwargs)

    @auth
    def delete_series(self, id_, **kwargs):
        return self.series.del_part(path_kwargs={"id": id_}, **kwargs)

    @auth
    def anonymize_series(self, id_, data={}, **kwargs):
        j = self.convert_to_json(data)
        return self.series.anonymize(path_kwargs={"id": id_}, data=j, **kwargs)

    @auth
    def get_series_archive(self, id_, **kwargs):
        return self.series.archive(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_series_instances(self, id_, **kwargs):
        return self.series.instances(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_series_instances_tags(self, id_, **kwargs):
        return self.series.instances_tags(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_series_media(self, id_, **kwargs):
        return self.series.media(path_kwargs={"id": id_}, **kwargs)

    @auth
    def modify_series(self, id_, data, **kwargs):
        j = self.convert_to_json(data)
        return self.series.modify(path_kwargs={"id": id_}, data=j, **kwargs)

    @auth
    def get_series_module(self, id_, **kwargs):
        return self.series.module(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_series_ordered_slices(self, id_, **kwargs):
        return self.series.ordered_slices(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_series_patient(self, id_, **kwargs):
        return self.series.patient(path_kwargs={"id": id_}, **kwargs)

    @auth
    def reconstruct_series(self, id_, **kwargs):
        return self.series.reconstruct(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_series_shared_tags(self, id_, **kwargs):
        return self.series.shared_tags(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_series_statistics(self, id_, **kwargs):
        return self.series.statistics(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_series_study(self, id_, **kwargs):
        return self.series.study(path_kwargs={"id": id_}, **kwargs)

    #### STUDIES
    @auth
    def get_studies(self, **kwargs):
        return self.studies.studies(**kwargs)

    @auth
    def get_study(self, id_, **kwargs):
        return self.studies.study(path_kwargs={"id": id_}, **kwargs)

    @auth
    def delete_study(self, id_, **kwargs):
        return self.studies.del_study(path_kwargs={"id": id_}, **kwargs)

    @auth
    def anonymize_study(self, id_, data={}, **kwargs):
        j = self.convert_to_json(data)
        return self.studies.anonymize(path_kwargs={"id": id_}, data=j, **kwargs)

    @auth
    def get_study_archive(self, id_, **kwargs):
        return self.studies.archive(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_study_instances(self, id_, **kwargs):
        return self.studies.instances(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_study_instances_tags(self, id_, **kwargs):
        return self.studies.instances_tags(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_study_media(self, id_, **kwargs):
        return self.studies.media(path_kwargs={"id": id_}, **kwargs)

    @auth
    def modify_study(self, id_, data, **kwargs):
        j = self.convert_to_json(data)
        return self.studies.modify(path_kwargs={"id": id_}, data=j, **kwargs)

    @auth
    def get_study_module(self, id_, **kwargs):
        return self.studies.module(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_study_module_patient(self, id_, **kwargs):
        return self.studies.module_patient(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_study_patient(self, id_, **kwargs):
        return self.studies.patient(path_kwargs={"id": id_}, **kwargs)

    @auth
    def reconstruct_study(self, id_, **kwargs):
        return self.studies.reconstruct(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_study_series(self, id_, **kwargs):
        return self.studies.series(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_study_shared_tags(self, id_, **kwargs):
        return self.studies.shared_tags(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_study_statistics(self, id_, **kwargs):
        return self.studies.statistics(path_kwargs={"id": id_}, **kwargs)

    #### MODALITIES ###
    @auth
    def get_modalities(self, **kwargs):
        return self.modalities.modalities(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_modality(self, dicom, **kwargs):
        return self.modalities.modality(path_kwargs={"dicom": dicom}, **kwargs)

    @auth
    def delete_modality(self, dicom, **kwargs):
        return self.modalities.del_modality(path_kwargs={"dicom": dicom}, **kwargs)

    @auth
    def update_modality(self, dicom, data, **kwargs):
        j = self.dumps(data)
        return self.modalities.put_modality(
            path_kwargs={"dicom": dicom}, data=j, **kwargs
        )

    @auth
    def echo_modality(self, dicom, **kwargs):
        return self.modalities.echo(path_kwargs={"dicom": dicom}, data={}, **kwargs)

    @auth
    def move_modality(self, dicom, data, **kwargs):
        j = self.dumps(data)
        return self.modalities.move(path_kwargs={"dicom": dicom}, data=j, **kwargs)

    @auth
    def query_modality(self, dicom, data, **kwargs):
        j = self.dumps(data)
        return self.modalities.query(path_kwargs={"dicom": dicom}, data=j, **kwargs)

    @auth
    def store_modality(self, dicom, data, **kwargs):
        j = self.dumps(data)
        return self.modalities.store(path_kwargs={"dicom": dicom}, data=j, **kwargs)

    #### SERVER-RELATED
    @auth
    def get_changes(self, since=0, limit=100, last=False, **kwargs):
        if last:
            kwargs["params"] = {"last": ""}  # overrule
        else:
            kwargs["params"] = {"since": since, "limit": limit}  # overrule
        return self.server.changes(**kwargs)

    @auth
    def clear_changes(self, **kwargs):
        return self.server.del_changes(**kwargs)

    @auth
    def get_exports(self, **kwargs):
        return self.server.exports(**kwargs)

    @auth
    def clear_exports(self, **kwargs):
        return self.server.del_exports(**kwargs)

    @auth
    def get_jobs(self, **kwargs):
        return self.server.jobs(**kwargs)

    @auth
    def get_job(self, id_, **kwargs):
        return self.server.job(path_kwargs={"id": id_}, **kwargs)

    @auth
    def cancel_job(self, id_, **kwargs):
        return self.server.cancel_job(path_kwargs={"id": id_}, data={}, **kwargs)

    @auth
    def pause_job(self, id_, **kwargs):
        return self.server.pause_job(path_kwargs={"id": id_}, data={}, **kwargs)

    @auth
    def resubmit_job(self, id_, **kwargs):
        return self.server.resubmit_job(path_kwargs={"id": id_}, data={}, **kwargs)

    @auth
    def resume_job(self, id_, **kwargs):
        return self.server.resume_job(path_kwargs={"id": id_}, data={}, **kwargs)

    @auth
    def get_peers(self, **kwargs):
        return self.server.peers(**kwargs)

    @auth
    def get_peer(self, peer, **kwargs):
        return self.server.peer(path_kwargs={"peer": peer}, **kwargs)

    @auth
    def delete_peer(self, peer, **kwargs):
        return self.server.del_peer(path_kwargs={"peer": peer}, **kwargs)

    @auth
    def put_peer(self, peer, **kwargs):
        return self.server.put_peer(path_kwargs={"peer": peer}, **kwargs)

    @auth
    def store_peer(self, peer, **kwargs):
        return self.server.store_peer(path_kwargs={"peer": peer}, **kwargs)

    @auth
    def get_plugins(self, **kwargs):
        return self.server.plugins(**kwargs)

    @auth
    def get_plugin(self, id_, **kwargs):
        return self.server.plugin(path_kwargs={"id": id_}, **kwargs)

    @auth
    def get_plugins_js(self, **kwargs):
        return self.server.plugins_js(**kwargs)

    @auth
    def get_statistics(self, **kwargs):
        return self.server.statistics(**kwargs)

    @auth
    def get_system(self, **kwargs):
        return self.server.system(**kwargs)

    @auth
    def create_archive(self, **kwargs):
        return self.server.tools_create_archive(**kwargs)

    @auth
    def create_dicom(self, **kwargs):
        return self.server.tools_create_dicom(**kwargs)

    @auth
    def create_media(self, **kwargs):
        return self.server.tools_create_media(**kwargs)

    @auth
    def create_media_extended(self, **kwargs):
        return self.server.tools_create_media_extended(**kwargs)

    @auth
    def get_default_encoding(self, **kwargs):
        return self.server.tools_default_encoding(**kwargs)

    @auth
    def change_default_encoding(self, **kwargs):
        return self.server.tools_post_default_encoding(**kwargs)

    @auth
    def get_dicom_conformance(self, **kwargs):
        return self.server.tools_dicom_conformance(**kwargs)

    @auth
    def execute_script(self, script, **kwargs):
        j = self.convert_to_json(script)
        return self.server.tools_execute_script(data=j, **kwargs)

    @auth
    def find(self, query, **kwargs):
        j = self.convert_to_json(query)
        return self.server.tools_find(data=j, **kwargs)

    @auth
    def generate_uid(self, level, **kwargs):
        """
        Level must be 'patient', 'instance', 'series', or 'study'
        """
        j = self.convert_to_json({"level": level})
        return self.server.tools_generate_uid(data=j, **kwargs)

    @auth
    def invalidate_tags(self, **kwargs):
        return self.server.tools_invalidate_tags(**kwargs)

    @auth
    def lookup(self, lookup, **kwargs):
        return self.server.tools_lookup(data=lookup, **kwargs)

    @auth
    def get_now(self, **kwargs):
        return self.server.tools_now(**kwargs)

    @auth
    def get_now_local(self, **kwargs):
        return self.server.tools_now_local(**kwargs)

    @auth
    def reset(self, **kwargs):
        return self.server.tools_reset(data={}, **kwargs)

    @auth
    def shutdown(self, **kwargs):
        return self.server.tools_shutdown(data={}, **kwargs)
