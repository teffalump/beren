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
                    OrthancInstancesService,
                    OrthancModalitiesService,
                    OrthancPatientsService,
                    OrthancQueriesService,
                    OrthancSeriesService,
                    OrthancServerService,
                    OrthancStudiesService,
                    )
from apiron.client import ServiceCaller
from json import dumps
from functools import partial

__all__=['Orthanc']

class Orthanc:
    def __init__(self, server, auth=None, *args, **kwargs):
        self._target = server
        self._auth = auth
        self._instances = OrthancInstancesService(server, *args, **kwargs)
        self._modalities = OrthancModalitiesService(server, *args, **kwargs)
        self._patients = OrthancPatientsService(server, *args, **kwargs)
        self._queries = OrthancQueriesService(server, *args, **kwargs)
        self._series = OrthancSeriesService(server, *args, **kwargs)
        self._server = OrthancServerService(server, *args, **kwargs)
        self._studies = OrthancStudiesService(server, *args, **kwargs)
        self.instances = partial(ServiceCaller.call, self._instances, auth=self._auth)
        self.modalities = partial(ServiceCaller.call, self._modalities, auth=self._auth)
        self.patients = partial(ServiceCaller.call, self._patients, auth=self._auth)
        self.queries = partial(ServiceCaller.call, self._queries, auth=self._auth)
        self.series = partial(ServiceCaller.call, self._series, auth=self._auth)
        self.server = partial(ServiceCaller.call, self._server, auth=self._auth)
        self.studies = partial(ServiceCaller.call, self._studies, auth=self._auth)

    def __repr__(self):
        return '<Client for Orthanc REST API at {}>'.format(self._target)

    @staticmethod
    def convert_to_json(data, **kwargs):
        return dumps(data, **kwargs)

    #### INSTANCES
    def get_instances(self, **kwargs):
        return self.instances(self._instances.instances, **kwargs)

    def add_instance(self, dicom, **kwargs):
        return self.instances(self._instances.add_instance, data=dicom, **kwargs)

    def get_instance(self, id_, **kwargs):
        return self.instances(self._instances.instance, path_kwargs={'id': id_}, **kwargs)

    def delete_instance(self, id_, **kwargs):
        return self.instances(self._instances.del_instance, path_kwargs={'id': id_}, **kwargs)

    def anonymize_instance(self, id_, data={}, **kwargs):
        j = self.convert_to_json(data)
        return self.instances(self._instances.anonymize, path_kwargs={'id': id_}, data=j, **kwargs)

    def get_instance_content(self, id_, **kwargs):
        return self.instances(self._instances.content, path_kwargs={'id': id_}, **kwargs)

    def get_instance_content_raw_tag(self, id_, **kwargs):
        return self.instances(self._instances.content_raw_tag, path_kwargs={'id': id_}, **kwargs)

    def export_instance(self, id_, **kwargs):
        return self.instances(self._instances.export, path_kwargs={'id': id_}, data={}, **kwargs)

    def get_instance_file(self, id_, **kwargs):
        return self.instances(self._instances.file_, path_kwargs={'id': id_}, **kwargs)

    def get_instance_frames(self, id_, **kwargs):
        return self.instances(self._instances.frames, path_kwargs={'id': id_}, **kwargs)

    def get_instance_frame_int16(self, id_, frame, **kwargs):
        return self.instances(self._instances.frame_int16, path_kwargs={'id': id_, 'number': frame}, **kwargs)

    def get_instance_frame_uint16(self, id_, frame, **kwargs):
        return self.instances(self._instances.frame_uint16, path_kwargs={'id': id_, 'number': frame}, **kwargs)

    def get_instance_frame_uint8(self, id_, frame, **kwargs):
        return self.instances(self._instances.frame_uint8, path_kwargs={'id': id_, 'number': frame}, **kwargs)

    def get_instance_frame_matlab(self, id_, frame, **kwargs):
        return self.instances(self._instances.frame_matlab, path_kwargs={'id': id_, 'number': frame}, **kwargs)

    def get_instance_frame_preview(self, id_, frame, **kwargs):
        return self.instances(self._instances.frame_preview, path_kwargs={'id': id_, 'number': frame}, **kwargs)

    def get_instance_frame_raw(self, id_, frame, **kwargs):
        return self.instances(self._instances.frame_raw, path_kwargs={'id': id_, 'number': frame}, **kwargs)

    def get_instance_frame_raw_gz(self, id_, frame, **kwargs):
        return self.instances(self._instances.frame_raw_gz, path_kwargs={'id': id_, 'number': frame}, **kwargs)

    def get_instance_header(self, id_, **kwargs):
        return self.instances(self._instances.header, path_kwargs={'id': id_}, **kwargs)

    def get_instance_int16(self, id_, **kwargs):
        return self.instances(self._instances.image_int16, path_kwargs={'id': id_}, **kwargs)

    def get_instance_uint16(self, id_, **kwargs):
        return self.instances(self._instances.image_uint16, path_kwargs={'id': id_}, **kwargs)

    def get_instance_uint8(self, id_, **kwargs):
        return self.instances(self._instances.image_uint8, path_kwargs={'id': id_}, **kwargs)

    def get_instance_matlab(self, id_, **kwargs):
        return self.instances(self._instances.matlab, path_kwargs={'id': id_}, **kwargs)

    def modify_instance(self, id_, data, **kwargs):
        j = self.convert_to_json(data)
        return self.instances(self._instances.modify, path_kwargs={'id': id_}, data=j, **kwargs)

    def get_instance_module(self, id_, **kwargs):
        return self.instances(self._instances.module, path_kwargs={'id': id_}, **kwargs)

    def get_instance_patient(self, id_, **kwargs):
        return self.instances(self._instances.patient, path_kwargs={'id': id_}, **kwargs)

    def get_instance_pdf(self, id_, **kwargs):
        return self.instances(self._instances.pdf, path_kwargs={'id': id_}, **kwargs)

    def get_instance_preview(self, id_, **kwargs):
        return self.instances(self._instances.preview, path_kwargs={'id': id_}, **kwargs)

    def reconstruct_instance(self, id_, **kwargs):
        return self.instances(self._instances.reconstruct, path_kwargs={'id': id_}, data={}, **kwargs)
    def get_instance_series(self, id_, **kwargs):
        return self.instances(self._instances.series, path_kwargs={'id': id_}, **kwargs)

    def get_instance_simplified_tags(self, id_, **kwargs):
        return self.instances(self._instances.simplified_tags, path_kwargs={'id': id_}, **kwargs)

    def get_instance_statistics(self, id_, **kwargs):
        return self.instances(self._instances.statistics, path_kwargs={'id': id_}, **kwargs)

    def get_instance_study(self, id_, **kwargs):
        return self.instances(self._instances.study, path_kwargs={'id': id_}, **kwargs)

    def get_instance_tags(self, id_, **kwargs):
        return self.instances(self._instances.tags, path_kwargs={'id': id_}, **kwargs)

    #### PATIENTS
    def get_patients(self, **kwargs):
        return self.patients(self._patients.patients, **kwargs)

    def get_patient(self, id_, **kwargs):
        return self.patients(self._patients.patient, path_kwargs={'id': id_}, **kwargs)

    def delete_patient(self, id_, **kwargs):
        return self.patients(self._patients.del_patient, path_kwargs={'id': id_}, **kwargs)

    def anonymize_patient(self, id_, data={}, **kwargs):
        j = self.convert_to_json(data)
        return self.patients(self._patients.anonymize, path_kwargs={'id': id_}, data=j, **kwargs)

    def archive_patient(self, id_, **kwargs):
        return self.patients(self._patients.archive, path_kwargs={'id': id_}, **kwargs)

    def get_patient_instances(self, id_, **kwargs):
        return self.patients(self._patients.instances, path_kwargs={'id': id_}, **kwargs)

    def get_patient_instance_tags(self, id_, **kwargs):
        return self.patients(self._patients.instances_tags, path_kwargs={'id': id_}, **kwargs)

    def modify_patient(self, id_, data, **kwargs):
        j = self.convert_to_json(data)
        return self.patients(self._patients.modify, path_kwargs={'id': id_}, data=j, **kwargs)

    def get_patient_module(self, id_, **kwargs):
        return self.patients(self._patients.module, path_kwargs={'id': id_}, **kwargs)

    def get_patient_media(self, id_, **kwargs):
        return self.patients(self._patients.media, path_kwargs={'id': id_}, **kwargs)

    def get_patient_protected(self, id_, **kwargs):
        return self.patients(self._patients.protected, path_kwargs={'id': id_}, **kwargs)

    def put_patient_protected(self, id_, data={}, **kwargs):
        return self.patients(self._patients.put_protected, path_kwargs={'id': id_}, data=data, **kwargs)

    def reconstruct_patient(self, id_, data={}, **kwargs):
        return self.patients(self._patients.protected, path_kwargs={'id': id_}, data=data, **kwargs)

    def get_patient_series(self, id_, **kwargs):
        return self.patients(self._patients.series, path_kwargs={'id': id_}, **kwargs)

    def get_patient_shared_tags(self, id_, **kwargs):
        return self.patients(self._patients.shared_tags, path_kwargs={'id': id_}, **kwargs)

    def get_patient_statistics(self, id_, **kwargs):
        return self.patients(self._patients.statistics, path_kwargs={'id': id_}, **kwargs)

    def get_patient_studies(self, id_, **kwargs):
        return self.patients(self._patients.studies, path_kwargs={'id': id_}, **kwargs)

    def get_patient_id_from_uuid(self, id_, **kwargs):
        return self.patients(self._patients.patient, path_kwargs={'id': id_}, **kwargs).get('MainDicomTags').get('PatientID')

    def get_patient_studies_from_id(self, id_, **kwargs):
        try:
            return [self.get_patient_studies(patient) for patient in self.find({'Level': 'Patient', 'Limit': 1, 'Query': {'PatientID': id_}}, **kwargs)][0]
        except:
            return []

    #### QUERIES
    def get_queries(self, **kwargs):
        return self.queries(self._queries.queries, **kwargs)

    def get_query(self, id_, **kwargs):
        return self.queries(self._queries.query, path_kwargs={'id': id_}, **kwargs)

    def delete_query(self, id_, **kwargs):
        return self.queries(self._queries.del_query, path_kwargs={'id': id_}, **kwargs)

    def get_query_answers(self, id_, **kwargs):
        return self.queries(self._queries.query, path_kwargs={'id': id_}, **kwargs)

    def get_query_answers_content(self, id_, index, **kwargs):
        return self.queries(self._queries.answers_content, path_kwargs={'id': id_, 'index': index}, **kwargs)

    def post_query_answers_retrieve(self, id_, index, **kwargs):
        return self.queries(self._queries.answers_retrieve, path_kwargs={'id': id_, 'index': index}, **kwargs)

    def get_query_level(self, id_, **kwargs):
        return self.queries(self._queries.level, path_kwargs={'id': id_}, **kwargs)

    def get_query_modality(self, id_, **kwargs):
        return self.queries(self._queries.modality, path_kwargs={'id': id_}, **kwargs)

    def get_query_query(self, id_, **kwargs):
        return self.queries(self._queries.query_query, path_kwargs={'id': id_}, **kwargs)

    def post_query_retrieve(self, id_, **kwargs):
        return self.queries(self._queries.retrieve, path_kwargs={'id': id_}, **kwargs)

    #### SERIES
    def get_series(self, **kwargs):
        return self.series(self._series.series, **kwargs)

    def get_one_series(self, id_, **kwargs):
        return self.series(self._series.part, path_kwargs={'id': id_}, **kwargs)

    def delete_series(self, id_, **kwargs):
        return self.series(self._series.del_part, path_kwargs={'id': id_}, **kwargs)

    def anonymize_series(self, id_, data={}, **kwargs):
        j = self.convert_to_json(data)
        return self.series(self._series.anonymize, path_kwargs={'id': id_}, data=j, **kwargs)

    def get_series_archive(self, id_, **kwargs):
        return self.series(self._series.archive, path_kwargs={'id': id_}, **kwargs)

    def get_series_instances(self, id_, **kwargs):
        return self.series(self._series.instances, path_kwargs={'id': id_}, **kwargs)

    def get_series_instances_tags(self, id_, **kwargs):
        return self.series(self._series.instances_tags, path_kwargs={'id': id_}, **kwargs)

    def get_series_media(self, id_, **kwargs):
        return self.series(self._series.media, path_kwargs={'id': id_}, **kwargs)

    def modify_series(self, id_, data, **kwargs):
        j = self.convert_to_json(data)
        return self.series(self._series.modify, path_kwargs={'id': id_}, data=j, **kwargs)

    def get_series_module(self, id_, **kwargs):
        return self.series(self._series.module, path_kwargs={'id': id_}, **kwargs)

    def get_series_ordered_slices(self, id_, **kwargs):
        return self.series(self._series.ordered_slices, path_kwargs={'id': id_}, **kwargs)

    def get_series_patient(self, id_, **kwargs):
        return self.series(self._series.patient, path_kwargs={'id': id_}, **kwargs)

    def reconstruct_series(self, id_, **kwargs):
        return self.series(self._series.reconstruct, path_kwargs={'id': id_}, **kwargs)

    def get_series_shared_tags(self, id_, **kwargs):
        return self.series(self._series.shared_tags, path_kwargs={'id': id_}, **kwargs)

    def get_series_statistics(self, id_, **kwargs):
        return self.series(self._series.statistics, path_kwargs={'id': id_}, **kwargs)

    def get_series_study(self, id_, **kwargs):
        return self.series(self._series.study, path_kwargs={'id': id_}, **kwargs)

    #### STUDIES
    def get_studies(self, **kwargs):
        return self.studies(self._studies.studies, **kwargs)

    def get_study(self, id_, **kwargs):
        return self.studies(self._studies.study, path_kwargs={'id': id_}, **kwargs)

    def delete_study(self, id_, **kwargs):
        return self.studies(self._studies.del_study, path_kwargs={'id': id_}, **kwargs)

    def anonymize_study(self, id_, data={}, **kwargs):
        j = self.convert_to_json(data)
        return self.studies(self._studies.anonymize, path_kwargs={'id': id_}, data=j, **kwargs)

    def get_study_archive(self, id_, **kwargs):
        return self.studies(self._studies.archive, path_kwargs={'id': id_}, **kwargs)

    def get_study_instances(self, id_, **kwargs):
        return self.studies(self._studies.instances, path_kwargs={'id': id_}, **kwargs)

    def get_study_instances_tags(self, id_, **kwargs):
        return self.studies(self._studies.instances_tags, path_kwargs={'id': id_}, **kwargs)

    def get_study_media(self, id_, **kwargs):
        return self.studies(self._studies.media, path_kwargs={'id': id_}, **kwargs)

    def modify_study(self, id_, data, **kwargs):
        j = self.convert_to_json(data)
        return self.studies(self._studies.modify, path_kwargs={'id': id_}, data=j, **kwargs)

    def get_study_module(self, id_, **kwargs):
        return self.studies(self._studies.module, path_kwargs={'id': id_}, **kwargs)

    def get_study_module_patient(self, id_, **kwargs):
        return self.studies(self._studies.module_patient, path_kwargs={'id': id_}, **kwargs)

    def get_study_patient(self, id_, **kwargs):
        return self.studies(self._studies.patient, path_kwargs={'id': id_}, **kwargs)

    def reconstruct_study(self, id_, **kwargs):
        return self.studies(self._studies.reconstruct, path_kwargs={'id': id_}, **kwargs)

    def get_study_series(self, id_, **kwargs):
        return self.studies(self._studies.series, path_kwargs={'id': id_}, **kwargs)

    def get_study_shared_tags(self, id_, **kwargs):
        return self.studies(self._studies.shared_tags, path_kwargs={'id': id_}, **kwargs)

    def get_study_statistics(self, id_, **kwargs):
        return self.studies(self._studies.statistics, path_kwargs={'id': id_}, **kwargs)

    #### MODALITIES ###
    def get_modalities(self, **kwargs):
        return self.modalities(self._modalities.modalities, path_kwargs={'id': id_}, **kwargs)

    def get_modality(self, dicom, **kwargs):
        return self.modalities(self._modalities.modality, path_kwargs={'dicom': dicom}, **kwargs)

    def delete_modality(self, dicom, **kwargs):
        return self.modalities(self._modalities.del_modality, path_kwargs={'dicom': dicom}, **kwargs)

    def update_modality(self, dicom, data, **kwargs):
        j = self.dumps(data)
        return self.modalities(self._modalities.put_modality, path_kwargs={'dicom': dicom}, data=j, **kwargs)

    def echo_modality(self, dicom, **kwargs):
        return self.modalities(self._modalities.echo, path_kwargs={'dicom': dicom}, data={}, **kwargs)

    def move_modality(self, dicom, data, **kwargs):
        j = self.dumps(data)
        return self.modalities(self._modalities.move, path_kwargs={'dicom': dicom}, data=j, **kwargs)

    def query_modality(self, dicom, data, **kwargs):
        j = self.dumps(data)
        return self.modalities(self._modalities.query, path_kwargs={'dicom': dicom}, data=j, **kwargs)

    def store_modality(self, dicom, data, **kwargs):
        j = self.dumps(data)
        return self.modalities(self._modalities.store, path_kwargs={'dicom': dicom}, data=j, **kwargs)

    #### SERVER-RELATED
    def get_changes(self, since=0, limit=100, last=False, **kwargs):
        if last:
            kwargs['params'] = {'last': ''} #overrule
        else:
            kwargs['params'] = {'since': since, 'limit': limit} #overrule
        return self.server(self._server.changes, **kwargs)

    def clear_changes(self, **kwargs):
        return self.server(self._server.del_changes, **kwargs)

    def get_exports(self, **kwargs):
        return self.server(self._server.exports, **kwargs)

    def clear_exports(self, **kwargs):
        return self.server(self._server.del_exports, **kwargs)

    def get_jobs(self, **kwargs):
        return self.server(self._server.jobs, **kwargs)

    def get_job(self, id_, **kwargs):
        return self.server(self._server.job, path_kwargs={'id': id_}, **kwargs)

    def cancel_job(self, id_, **kwargs):
        return self.server(self._server.cancel_job, path_kwargs={'id': id_}, data={}, **kwargs)

    def pause_job(self, id_,  **kwargs):
        return self.server(self._server.pause_job, path_kwargs={'id': id_}, data={}, **kwargs)

    def resubmit_job(self, id_, **kwargs):
        return self.server(self._server.resubmit_job, path_kwargs={'id': id_}, data={}, **kwargs)

    def resume_job(self, id_, **kwargs):
        return self.server(self._server.resume_job, path_kwargs={'id': id_}, data={}, **kwargs)

    def get_peers(self, **kwargs):
        return self.server(self._server.peers, **kwargs)

    def get_peer(self, peer, **kwargs):
        return self.server(self._server.peer, path_kwargs={'peer': peer}, **kwargs)

    def delete_peer(self, peer, **kwargs):
        return self.server(self._server.del_peer, path_kwargs={'peer': peer}, **kwargs)

    def put_peer(self, peer, **kwargs):
        return self.server(self._server.put_peer, path_kwargs={'peer': peer}, **kwargs)

    def store_peer(self, peer, **kwargs):
        return self.server(self._server.store_peer, path_kwargs={'peer': peer}, **kwargs)

    def get_plugins(self, **kwargs):
        return self.server(self._server.plugins, **kwargs)

    def get_plugin(self, id_, **kwargs):
        return self.server(self._server.plugin, path_kwargs={'id': id_}, **kwargs)

    def get_plugins_js(self, **kwargs):
        return self.server(self._server.plugins_js, **kwargs)

    def get_statistics(self, **kwargs):
        return self.server(self._server.statistics, **kwargs)

    def get_system(self, **kwargs):
        return self.server(self._server.system, **kwargs)

    def create_archive(self, **kwargs):
        return self.server(self._server.tools_create_archive, **kwargs)

    def create_dicom(self, **kwargs):
        return self.server(self._server.tools_create_dicom, **kwargs)

    def create_media(self, **kwargs):
        return self.server(self._server.tools_create_media, **kwargs)

    def create_media_extended(self, **kwargs):
        return self.server(self._server.tools_create_media_extended, **kwargs)

    def get_default_encoding(self, **kwargs):
        return self.server(self._server.tools_default_encoding, **kwargs)

    def change_default_encoding(self, **kwargs):
        return self.server(self._server.tools_post_default_encoding, **kwargs)

    def get_dicom_conformance(self, **kwargs):
        return self.server(self._server.tools_dicom_conformance, **kwargs)

    def execute_script(self, script, **kwargs):
        j = self.convert_to_json(script)
        return self.server(self._server.tools_execute_script, data=j, **kwargs)

    def find(self, query, **kwargs):
        j = self.convert_to_json(query)
        return self.server(self._server.tools_find, data=j, **kwargs)

    def generate_uid(self, level, **kwargs):
        '''
        Level must be 'patient', 'instance', 'series', or 'study'
        '''
        j = self.convert_to_json({'level': level})
        return self.server(self._server.tools_generate_uid, data=j, **kwargs)

    def invalidate_tags(self, **kwargs):
        return self.server(self._server.tools_invalidate_tags, **kwargs)

    def lookup(self, lookup, **kwargs):
        return self.server(self._server.tools_lookup, data=lookup, **kwargs)

    def get_now(self, **kwargs):
        return self.server(self._server.tools_now, **kwargs)

    def get_now_local(self, **kwargs):
        return self.server(self._server.tools_now_local, **kwargs)

    def reset(self, **kwargs):
        return self.server(self._server.tools_reset, data={}, **kwargs)

    def shutdown(self, **kwargs):
        return self.server(self._server.tools_shutdown, data={}, **kwargs)
