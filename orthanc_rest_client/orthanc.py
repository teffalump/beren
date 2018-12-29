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

from orthanc_rest_client.endpoints import (
                                        OrthancPatientsService,
                                        OrthancInstancesService,
                                        OrthancSeriesService,
                                        OrthancStudiesService,
                                        OrthancQueriesService,
                                        OrthancServerService,
                                        )
from apiron.client import ServiceCaller

__all__=['Orthanc']

class Orthanc:
    def __init__(self, server, *args, **kwargs):
        self.instances = OrthancInstancesService(server, *args, **kwargs)
        self.patients = OrthancPatientsService(server, *args, **kwargs)
        self.series = OrthancSeriesService(server, *args, **kwargs)
        self.studies = OrthancStudiesService(server, *args, **kwargs)
        self.queries = OrthancQueriesService(server, *args, **kwargs)
        self.server = OrthancServerService(server, *args, **kwargs)

    #### INSTANCES
    def get_instances(self, **kwargs):
        return ServiceCaller.call(self.instances, self.instances.instances, **kwargs)

    def add_instance(self, dicom, **kwargs):
        return ServiceCaller.call(self.instances, self.instances.add_instance, data=dicom, **kwargs)

    def get_instance(self, id_, **kwargs):
        return ServiceCaller.call(self.instances, self.instances.instance, path_kwargs={'id': id_}, **kwargs)

    def delete_instance(self, id_, **kwargs):
        return ServiceCaller.call(self.instances, self.instances.del_instance, path_kwargs={'id': id_}, **kwargs)

    def anonymize_instance(self, id_, data={}, **kwargs):
        return ServiceCaller.call(self.instances, self.instances.del_instance, path_kwargs={'id': id_}, data=data, **kwargs)

    def get_instance_patient(self, id_, **kwargs):
        return ServiceCaller.call(self.instances, self.instances.instance_patient, path_kwargs={'id': id_}, **kwargs)

    def get_instance_statistics(self, id_, **kwargs):
        return ServiceCaller.call(self.instances, self.instances.statistics, path_kwargs={'id': id_}, **kwargs)

    def get_instance_study(self, id_, **kwargs):
        return ServiceCaller.call(self.instances, self.instances.study, path_kwargs={'id': id_}, **kwargs)

    #### PATIENTS
    def get_patients(self, **kwargs):
        return ServiceCaller.call(self.patients, self.patients.patients, **kwargs)

    def get_patient(self, id_, **kwargs):
        return ServiceCaller.call(self.patients, self.patients.patient, path_kwargs={'id': id_}, **kwargs)

    def delete_patient(self, id_, **kwargs):
        return ServiceCaller.call(self.patients, self.patients.del_patient, path_kwargs={'id': id_}, **kwargs)

    def anonymize_patient(self, id_, **kwargs):
        return ServiceCaller.call(self.patients, self.patients.anonymize, path_kwargs={'id': id_}, **kwargs)

    def archive_patient(self, id_, **kwargs):
        return ServiceCaller.call(self.patients, self.service.archive, path_kwargs={'id': id_}, **kwargs)

    def get_patient_instances(self, id_, **kwargs):
        return ServiceCaller.call(self.patients, self.service.instances, path_kwargs={'id': id_}, **kwargs)

    def get_patient_instance_tags(self, id_, **kwargs):
        return ServiceCaller.call(self.patients, self.service.instances_tags, path_kwargs={'id': id_}, **kwargs)

    def modify_patient(self, id_, data, **kwargs):
        return ServiceCaller.call(self.patients, self.patients.modify, path_kwargs={'id': id_}, data=data, **kwargs)

    def get_patient_module(self, id_, **kwargs):
        return ServiceCaller.call(self.patients, self.patients.module, path_kwargs={'id': id_}, **kwargs)

    def get_patient_media(self, id_, **kwargs):
        return ServiceCaller.call(self.patients, self.patients.media, path_kwargs={'id': id_}, **kwargs)

    def get_patient_protected(self, id_, **kwargs):
        return ServiceCaller.call(self.patients, self.patients.protected, path_kwargs={'id': id_}, **kwargs)

    def put_patient_protected(self, id_, data={}, **kwargs):
        return ServiceCaller.call(self.patients, self.patients.put_protected, path_kwargs={'id': id_}, data=data, **kwargs)

    def reconstruct_patient(self, id_, data={}, **kwargs):
        return ServiceCaller.call(self.patients, self.patients.protected, path_kwargs={'id': id_}, data=data, **kwargs)

    def get_patient_series(self, id_, **kwargs):
        return ServiceCaller.call(self.patients, self.patients.series, path_kwargs={'id': id_}, **kwargs)

    def get_patient_shared_tags(self, id_, **kwargs):
        return ServiceCaller.call(self.patients, self.patients.shared_tags, path_kwargs={'id': id_}, **kwargs)

    def get_patient_statistics(self, id_, **kwargs):
        return ServiceCaller.call(self.patients, self.patients.statistics, path_kwargs={'id': id_}, **kwargs)

    def get_patient_studies(self, id_, **kwargs):
        return ServiceCaller.call(self.patients, self.patients.studies, path_kwargs={'id': id_}, **kwargs)

    def get_patient_id_from_uuid(self, id_, **kwargs):
        return ServiceCaller.call(self.patients, self.patients.patient, path_kwargs={'id': id_}, **kwargs).get('MainDicomTags').get('PatientID')

    def get_patient_studies_from_id(self, id_, **kwargs):
        try:
            return [self.get_patient_studies(patient) for patient in self.find({'Level': 'Patient', 'Limit': 1, 'Query': {'PatientID': id_}}, **kwargs)][0]
        except:
            return []

    #### QUERIES
    def get_queries(self, **kwargs):
        return ServiceCaller.call(self.queries, self.queries.queries, **kwargs)

    def get_query(self, id_, **kwargs):
        return ServiceCaller.call(self.queries, self.queries.query, path_kwargs={'id': id_}, **kwargs)

    def delete_query(self, id_, **kwargs):
        return ServiceCaller.call(self.queries, self.queries.del_query, path_kwargs={'id': id_}, **kwargs)

    def get_query_answers(self, id_, **kwargs):
        return ServiceCaller.call(self.queries, self.queries.query, path_kwargs={'id': id_}, **kwargs)

    def get_query_answers_content(self, id_, index, **kwargs):
        return ServiceCaller.call(self.queries, self.queries.answers_content, path_kwargs={'id': id_, 'index': index}, **kwargs)

    def post_query_answers_retrieve(self, id_, index, **kwargs):
        return ServiceCaller.call(self.queries, self.queries.answers_retrieve, path_kwargs={'id': id_, 'index': index}, **kwargs)

    def get_query_level(self, id_, **kwargs):
        return ServiceCaller.call(self.queries, self.queries.level, path_kwargs={'id': id_}, **kwargs)

    def get_query_modality(self, id_, **kwargs):
        return ServiceCaller.call(self.queries, self.queries.modality, path_kwargs={'id': id_}, **kwargs)

    def get_query_query(self, id_, **kwargs):
        return ServiceCaller.call(self.queries, self.queries.query_query, path_kwargs={'id': id_}, **kwargs)

    def post_query_retrieve(self, id_, **kwargs):
        return ServiceCaller.call(self.queries, self.queries.retrieve, path_kwargs={'id': id_}, **kwargs)

    #### SERIES
    def get_series(self, **kwargs):
        return ServiceCaller.call(self.series, self.series.series, **kwargs)

    def get_one_series(self, id_, **kwargs):
        return ServiceCaller.call(self.series, self.series.part, path_kwargs={'id': id_}, **kwargs)

    def delete_series(self, id_, **kwargs):
        return ServiceCaller.call(self.series, self.series.del_part, path_kwargs={'id': id_}, **kwargs)

    def anonymize_series(self, id_, **kwargs):
        return ServiceCaller.call(self.series, self.series.anonymize, path_kwargs={'id': id_}, **kwargs)

    def get_series_archive(self, id_, **kwargs):
        return ServiceCaller.call(self.series, self.series.archive, path_kwargs={'id': id_}, **kwargs)

    def get_series_instances(self, id_, **kwargs):
        return ServiceCaller.call(self.series, self.series.instances, path_kwargs={'id': id_}, **kwargs)

    def get_series_instances_tags(self, id_, **kwargs):
        return ServiceCaller.call(self.series, self.series.instances_tags, path_kwargs={'id': id_}, **kwargs)

    def get_series_media(self, id_, **kwargs):
        return ServiceCaller.call(self.series, self.series.media, path_kwargs={'id': id_}, **kwargs)

    def modify_series(self, id_, **kwargs):
        return ServiceCaller.call(self.series, self.series.modify, path_kwargs={'id': id_}, **kwargs)

    def get_series_module(self, id_, **kwargs):
        return ServiceCaller.call(self.series, self.series.module, path_kwargs={'id': id_}, **kwargs)

    def get_series_ordered_slices(self, id_, **kwargs):
        return ServiceCaller.call(self.series, self.series.ordered_slices, path_kwargs={'id': id_}, **kwargs)

    def get_series_patient(self, id_, **kwargs):
        return ServiceCaller.call(self.series, self.series.patient, path_kwargs={'id': id_}, **kwargs)

    def reconstruct_series(self, id_, **kwargs):
        return ServiceCaller.call(self.series, self.series.reconstruct, path_kwargs={'id': id_}, **kwargs)

    def get_series_shared_tags(self, id_, **kwargs):
        return ServiceCaller.call(self.series, self.series.shared_tags, path_kwargs={'id': id_}, **kwargs)

    def get_series_statistics(self, id_, **kwargs):
        return ServiceCaller.call(self.series, self.series.statistics, path_kwargs={'id': id_}, **kwargs)

    def get_series_study(self, id_, **kwargs):
        return ServiceCaller.call(self.series, self.series.study, path_kwargs={'id': id_}, **kwargs)

    #### STUDIES
    def get_studies(self, **kwargs):
        return ServiceCaller.call(self.studies, self.studies.studies, **kwargs)

    def get_study(self, id_, **kwargs):
        return ServiceCaller.call(self.studies, self.studies.sudy, path_kwargs={'id': id_}, **kwargs)

    def delete_study(self, id_, **kwargs):
        return ServiceCaller.call(self.studies, self.studies.del_study, path_kwargs={'id': id_}, **kwargs)

    def anonymize_study(self, id_, **kwargs):
        return ServiceCaller.call(self.studies, self.studies.anonymize, path_kwargs={'id': id_}, **kwargs)

    def get_study_archive(self, id_, **kwargs):
        return ServiceCaller.call(self.studies, self.studies.archive, path_kwargs={'id': id_}, **kwargs)

    def get_study_instances(self, id_, **kwargs):
        return ServiceCaller.call(self.studies, self.studies.instances, path_kwargs={'id': id_}, **kwargs)

    def get_study_instances_tags(self, id_, **kwargs):
        return ServiceCaller.call(self.studies, self.studies.instances_tags, path_kwargs={'id': id_}, **kwargs)

    def get_study_media(self, id_, **kwargs):
        return ServiceCaller.call(self.studies, self.studies.media, path_kwargs={'id': id_}, **kwargs)

    def modify_study(self, id_, **kwargs):
        return ServiceCaller.call(self.studies, self.studies.modify, path_kwargs={'id': id_}, **kwargs)

    def get_study_module(self, id_, **kwargs):
        return ServiceCaller.call(self.studies, self.studies.module, path_kwargs={'id': id_}, **kwargs)

    def get_study_module_patient(self, id_, **kwargs):
        return ServiceCaller.call(self.studies, self.studies.module_patient, path_kwargs={'id': id_}, **kwargs)

    def get_study_patient(self, id_, **kwargs):
        return ServiceCaller.call(self.studies, self.studies.patient, path_kwargs={'id': id_}, **kwargs)

    def reconstruct_study(self, id_, **kwargs):
        return ServiceCaller.call(self.studies, self.studies.reconstruct, path_kwargs={'id': id_}, **kwargs)

    def get_study_series(self, id_, **kwargs):
        return ServiceCaller.call(self.studies, self.studies.series, path_kwargs={'id': id_}, **kwargs)

    def get_study_shared_tags(self, id_, **kwargs):
        return ServiceCaller.call(self.studies, self.studies.shared_tags, path_kwargs={'id': id_}, **kwargs)

    def get_study_statistics(self, id_, **kwargs):
        return ServiceCaller.call(self.studies, self.studies.statistics, path_kwargs={'id': id_}, **kwargs)

    #### SERVER-RELATED
