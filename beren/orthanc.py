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

from beren.endpoints import (
    OrthancInstances,
    OrthancModalities,
    OrthancPatients,
    OrthancQueries,
    OrthancSeries,
    OrthancServer,
    OrthancStudies,
)
from json import dumps
from warnings import warn
from urllib.parse import urlparse

__all__ = ["Orthanc"]


class Orthanc:
    """
    A class for interfacing with Orthanc DICOM REST APIs.

    :param str server:
        Fully qualified URL of the API
    :param requests.auth.HTTPBasicAuth auth:
        Auth object from :mod:`requests` with server credentials (optional)
    :param bool warn_insecure:
        Warn on HTTP endpoints (default: True)
    :return:
        A class with robust methods to interact with the REST API
    :rtype:
        class
    """

    def __init__(self, server, auth=None, warn_insecure=True):
        self._target = server
        self._auth = auth
        self.instances = OrthancInstances
        self.modalities = OrthancModalities
        self.patients = OrthancPatients
        self.queries = OrthancQueries
        self.series = OrthancSeries
        self.server = OrthancServer
        self.studies = OrthancStudies

        if urlparse(server)[0] == "http" and warn_insecure:
            warn(
                """{} is an unencrypted connection! Strongly consider using an encrypted (https) REST endpoint.""".format(
                    server
                )
            )

        # Set target and auth for each apiron service
        for x in [
            self.instances,
            self.modalities,
            self.patients,
            self.queries,
            self.series,
            self.server,
            self.studies,
        ]:
            setattr(x, "domain", self._target)
            setattr(x, "auth", self._auth)

    def __repr__(self):
        return "<Orthanc REST client({})>".format(self._target)

    @classmethod
    def get_api_methods(cls):
        """List callable endpoints"""
        return [
            func
            for func in dir(cls)
            if callable(getattr(cls, func))
            and not func.startswith("__")
            and func
            not in [
                "clean",
                "convert_to_json",
                "build_root_parameters",
                "get_api_methods",
            ]
        ]

    @staticmethod
    def convert_to_json(data, **kwargs):
        """Wrapper for ``json.dumps``"""
        return dumps(data, **kwargs)

    @staticmethod
    def clean(d):
        """Clean the parameter dict for endpoint semantics

        Accordingly,
            Boolean True is converted to 1, False is dropped
            Values evaluating to None are dropped
            Keep the other entries

        :param dict d
            Dictinary to clean
        :return
            Cleaned dictionary
        :rtype:
            dict
        """

        n = {}
        for k, v in d.items():
            if isinstance(v, (bool)):
                if v == True:
                    n[k] = 1
            elif v == None:
                continue
            else:
                n[k] = v
        return n

    @classmethod
    def build_root_parameters(cls, expand, since, limit, params):
        """Helper function for root endpoints' (/study, /patient, /instance, /series) parameter logic"""
        if params is None:
            passed_params = {}
            if expand == True:
                passed_params["expand"] = True
            if limit is not None or since is not None:
                try:
                    passed_params["since"] = int(since)
                    passed_params["limit"] = int(limit)
                except:
                    passed_params.pop("since", None)
                    passed_params.pop("limit", None)
                    warn("Must provide valid integers to since AND limit. Ignoring.")
            return cls.clean(passed_params)
        else:
            return params

    #### INSTANCES
    def get_instances(
        self, expand=False, since=None, limit=None, params=None, **kwargs
    ):
        """Return instance record(s). No raw file data.

        Use ``expand`` keyword argument to retrieve extensive information.
        Use ``since`` and ``limit`` keyword arguments to specify a group of records.

        :param bool expand:
            Return verbose information about instances. Default ``False``.
            By default, returns UUIDs.
        :param int since:
            Return since nth instance record. Optional. Must use with ``limit``.
        :param int limit:
            Limit to given number of records. Optional. Must use with ``since``.
        :param dict params:
            Provide overriding parameter dictionary
        :return:
            A list of records: either UUIDs or dictionary of information
        :rtype:
            list
        """
        kwargs["params"] = self.build_root_parameters(expand, since, limit, params)
        return self.instances.instances(**kwargs)

    def add_instance(self, dicom, **kwargs):
        """Add DICOM instance.

        :param data dicom:
            DICOM data
        :return:
            Response status
        :rtype:
            dict
        """
        return self.instances.add_instance(data=dicom, **kwargs)

    def get_instance(self, id_, **kwargs):
        """Get a single instance record. Equivalent to ``expand``.

        No raw data - use ``get_instance_file`` instead

        :param str id_:
            The instance UUID
        :return:
            Instance information
        :rtype:
            dict
        """
        return self.instances.instance(id_=id_, **kwargs)

    def delete_instance(self, id_, **kwargs):
        """Delete an instance

        :param str id_:
            Instance UUID
        :return
            Success or not
        :rtype:
            dict
        """
        return self.instances.del_instance(id_=id_, **kwargs)

    def anonymize_instance(
        self,
        id_,
        version="2017c",
        keep_private=False,
        keep_tags=None,
        replace_tags=None,
        **kwargs
    ):
        """Anonymize the instance by erasing all the tags that are specified in Table E.1-1 from PS 3.15 of the DICOM standard


        :param str id_:
            The instance UUID
        :param str version:
            DICOM Standard "2017c" (default) or "2008"
        :param bool keep_private:
            Keep manufacturer specific tags (can have patient information) (default False)
        :param list keep_tags:
            Keep these tags
        :param dict replace_tags:
            Replace these tags with new values {"PatientName": "FakeBob", etc}
        :return:
            Anonymized DICOM file
        :rtype:
            generator
        """
        data = self.clean(
            {
                "DicomVersion": version,
                "KeepPrivateTags": keep_private,
                "Keep": keep_tags,
                "Replace": replace_tags,
            }
        )
        return self.instances.anonymize(id_=id_, json=data, **kwargs)

    def get_instance_content(self, id_, **kwargs):
        """List first-level DICOM tags.

        :param str id_:
            The instance UUID
        :return:
            The first-level DICOM tags.
        :rtype:
            list
        """
        return self.instances.content(id_=id_, **kwargs)

    def get_instance_content_raw_tag(self, id_, group, element, **kwargs):
        """Get raw access to the DICOM tag (comprising the padding character)

        :param str id_:
            The instance UUID
        :param str group:
            The group
        :param str element:
            The element
        :return:
            The raw DICOM tag
        :rtype:
            str
        """
        return self.instances.content_raw_tag(
            id_=id_, group=group, element=element, **kwargs
        )

    def export_instance(self, id_, **kwargs):
        """Write the DICOM file to the filesystem where Orthanc is running

        :param str id_:
            The instance UUID
        :return:
            Empty list
        :rtype:
            list
        """
        return self.instances.export(id_=id_, data={}, **kwargs)

    def get_instance_file(self, id_, **kwargs):
        """Get the instance file

        Example:

            >>> for x in orthanc.get_instance_file(<id>):
            ...     print(x)

        :param str id_:
            The instance UUID
        :return:
            Yields the raw DICOM file
        :rtype:
            generator
        """
        return self.instances.file_(id_=id_, **kwargs)

    def get_instance_frame(self, id_, frame, format_, **kwargs):
        """Get an instance frame in specified format

        :param str id_:
            The instance UUID
        :param int frame:
            Frame number
        :param str format_:
            "image-uint8", "image-uint16", "image-int16", "matlab", "raw", or "raw.gz"
        :return:
            Frame
        :return:
            generator
        """
        return self.instances.frame(id_=id_, frame=frame, format_=format_, **kwargs)

    def get_instance_frames(self, id_, **kwargs):
        """Get the list of frame numbers in the instance file.

        :param str id_:
            The instance UUID
        :return:
            A list of integers corresponding to the frames
        :rtype:
            list (int)
        """
        return self.instances.frames(id_=id_, **kwargs)

    def get_instance_frame_preview(self, id_, frame, **kwargs):
        """Download preview image of instance frame

        :param str id_:
            The instance UUID
        :param int frame:
            Frame number
        :return:
            Image
        :rtype:
            generator
        """
        return self.instances.frame_preview(id_=id_, number=frame, **kwargs)

    def get_instance_header(self, id_, simplify=False, short=False, **kwargs):
        """Get detailed header tags for DICOM instance

        :param str id_:
            Instance UUID
        :param bool simplify:
            Equivalent to simplified-tags
        :param bool short:
            Shorten values without user-friendly descriptions of the the tag and type. Direct values to tags
        :return:
            Detailed tags and values
        :rtype:
            dict
        """
        kwargs["params"] = self.clean({"simplify": simplify, "short": short})
        return self.instances.header(id_=id_, **kwargs)

    def get_instance_image(self, id_, format_, **kwargs):
        """Download image of DICOM instance in specified format

        :param str id_:
            Instance UUID
        :param str format_:
            "image-uint8", "image-uint16", "image-int16", "matlab", "raw", or "raw.gz"
        :return:
            Image
        :rtype:
            generator
        """
        return self.instances.image(id_=id_, format_=format_, **kwargs)

    def modify_instance(
        self,
        id_,
        replace={},
        remove=[],
        remove_private_tags=False,
        force=False,
        **kwargs
    ):
        """Modify a set of specified tags in a single DICOM instance and download the resulting modified DICOM file

        :param str id_:
            Instance UUID
        :param dict replace:
            The dictionary which specifies the substitions to be applied (cf. anonymization). Default empty.
        :param list remove:
            List of tags to remove. Default empty.
        :param bool remove_private_tags:
            If set to true, the private tags (i.e. manufacturer-specific tags) are removed. Default False.
        :param bool force:
            The force option must be set to True in order to allow the modification of the PatientID, as such a modification of the DICOM identifiers might lead to breaking the DICOM model of the real-world. In general, any explicit modification to one of the PatientID, StudyInstanceUID, SeriesInstanceUID, and SOPInstanceUID requires Force to be set to True, in order to prevent any unwanted side effect. Default False.
        :return:
            DICOM file
        :rtype:
            generator
        """
        data = self.clean(
            {
                "Replace": replace,
                "Remove": remove,
                "RemovePrivateTags": remove_private_tags,
                "Force": force,
            }
        )
        return self.instances.modify(id_=id_, json=data, **kwargs)

    def get_instance_module(self, id_, **kwargs):
        return self.instances.module(id_=id_, **kwargs)

    def get_instance_patient(self, id_, **kwargs):
        """Get the parent patient of this instance.

        :param str id_:
            The instance UUID
        :return:
            The parent patient information
        :rtype:
            dict
        """
        return self.instances.patient(id_=id_, **kwargs)

    def get_instance_pdf(self, id_, **kwargs):
        """Download embedded PDF of DICOM instance

        :param str id_:
            The instance UUID
        :return:
            Embedded PDF or error
        :rtype:
            generator
        """
        return self.instances.pdf(id_=id_, **kwargs)

    def get_instance_preview(self, id_, png=True, **kwargs):
        """Download a preview image of the DICOM instance. Default "image/png". Other option "image/jpeg"

        :param str id_:
            Instance UUID
        :param bool png:
            Image format. Default png. False is jpeg.
        :return:
            DICOM preview
        :rtype:
            generator
        """
        image_type = "image/png" if png == True else "image/jpeg"
        return self.instances.preview(id_=id_, headers={"Accept": image_type}, **kwargs)

    def reconstruct_instance(self, id_, **kwargs):
        """Force reconstruction of the main DICOM tags, JSON summary and metadata

        :param str id_:
            Instance UUID
        :return:
            Empty list on success
        :rtype:
            List
        """
        return self.instances.reconstruct(id_=id_, data={}, **kwargs)

    def get_instance_series(self, id_, **kwargs):
        """Get the parent series of this instance.

        :param str id_:
            The instance UUID
        :return:
            The parent series information
        :rtype:
            dict
        """
        return self.instances.series(id_=id_, **kwargs)

    def get_instance_simplified_tags(self, id_, **kwargs):
        """Get human readable tags for the DICOM instance

        :param str id_:
            Instance UUID
        :return:
            DICOM tags and values
        :rtype:
            dict
        """
        return self.instances.simplified_tags(id_=id_, **kwargs)

    def get_instance_statistics(self, id_, **kwargs):
        """Get instance statistics

        :param str id_:
            Instance UUID
        :return:
            Instance statistics
        :rtype:
            dict
        """
        return self.instances.statistics(id_=id_, **kwargs)

    def get_instance_study(self, id_, **kwargs):
        """Get the parent study of this instance.

        :param str id_:
            The instance UUID
        :return:
            The parent study information
        :rtype:
            dict
        """
        return self.instances.study(id_=id_, **kwargs)

    def get_instance_tag(self, id_, tag, **kwargs):
        """Get the value for a single tag of a DICOM instance

        :param str id_:
            Instance UUID
        :param str tag:
            Instance tag
        :return:
            Tag value
        :rtype:
            dict
        """
        return self.instances.tags(id_=id_, tag=tag, **kwargs)

    def get_instance_tags(self, id_, simplify=False, short=False, **kwargs):
        """Get the detailed tags for the DICOM instance

        :param str id_:
            Instance UUID
        :param bool simplify:
            Equivalent to simplified-tags
        :param bool short:
            Shorten values without user-friendly descriptions of the the tag and type. Direct values to tags
        :return:
            Detailed tags and values
        :rtype:
            dict
        """
        kwargs["params"] = self.clean({"simplify": simplify, "short": short})
        return self.instances.tags(id_=id_, **kwargs)

    #### PATIENTS
    def get_patients(self, expand=False, since=None, limit=None, params=None, **kwargs):
        """Return patient record(s)

        Use ``expand`` keyword argument to retrieve expanded information.
        Use ``since`` and ``limit`` keyword arguments to specify group of records.

        :param bool expand:
            Return verbose information about patients. Default ``False``.
            By default, returns UUIDs.
        :param int since:
            Return since nth patient record. Optional. Must use with ``limit``.
        :param int limit:
            Limit to given number of records. Optional. Must use with ``since``.
        :param dict params:
            Provide paramaters dict to override other values
        :return:
            A list of records: either UUIDs or dictionary of information
        :rtype:
            list
        """
        kwargs["params"] = self.build_root_parameters(expand, since, limit, params)
        return self.patients.patients(**kwargs)

    def get_patient(self, id_, **kwargs):
        """Get a single patient record. Equivalent to ``expand``.

        :param str id_:
            The patient UUID
        :return:
            Expanded patient record
        :rtype:
            dict
        """
        return self.patients.patient(id_=id_, **kwargs)

    def delete_patient(self, id_, **kwargs):
        return self.patients.del_patient(id_=id_, **kwargs)

    def anonymize_patient(self, id_, data={}, **kwargs):
        return self.patients.anonymize(id_=id_, json=data, **kwargs)

    def archive_patient(self, id_, **kwargs):
        return self.patients.archive(id_=id_, **kwargs)

    def get_patient_instances(self, id_, **kwargs):
        """Get all instances for this patient

        :param str id_:
            Patient UUID
        :return:
            All the instances for this patient. Expanded information.
        :rtype:
            list (dict)
        """
        return self.patients.instances(id_=id_, **kwargs)

    def get_patient_instance_tags(self, id_, **kwargs):
        return self.patients.instances_tags(id_=id_, **kwargs)

    def modify_patient(self, id_, data, **kwargs):
        return self.patients.modify(id_=id_, json=data, **kwargs)

    def get_patient_module(self, id_, **kwargs):
        return self.patients.module(id_=id_, **kwargs)

    def get_patient_media(self, id_, **kwargs):
        return self.patients.media(id_=id_, **kwargs)

    def get_patient_protected(self, id_, **kwargs):
        return self.patients.protected(id_=id_, **kwargs)

    def put_patient_protected(self, id_, data={}, **kwargs):
        return self.patients.put_protected(id_=id_, data=data, **kwargs)

    def reconstruct_patient(self, id_, data={}, **kwargs):
        return self.patients.protected(id_=id_, data=data, **kwargs)

    def get_patient_series(self, id_, **kwargs):
        """Get all series for this patient

        :param str id_:
            Patient UUID
        :return:
            All the series for this patient. Expanded information.
        :rtype:
            list (dict)
        """
        return self.patients.series(id_=id_, **kwargs)

    def get_patient_shared_tags(self, id_, **kwargs):
        return self.patients.shared_tags(id_=id_, **kwargs)

    def get_patient_statistics(self, id_, **kwargs):
        return self.patients.statistics(id_=id_, **kwargs)

    def get_patient_studies(self, id_, **kwargs):
        """Get all studies for this patient

        :param str id_:
            Patient UUID
        :return:
            All the studies for this patient. Expanded information.
        :rtype:
            list (dict)
        """
        return self.patients.studies(id_=id_, **kwargs)

    def get_patient_id_from_uuid(self, id_, **kwargs):
        """Get the patient ID (usually equivalent to MRN/PUID) from UUID

        Helper function.

        :param str id:
            Patient UUID
        :return:
            The patient ID, usually equivalent to MRN/PUID
        :rtype:
            str
        """
        return (
            self.patients.patient(id_=id_, **kwargs)
            .get("MainDicomTags")
            .get("PatientID")
        )

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
    def get_queries(self, **kwargs):
        return self.queries.queries(**kwargs)

    def get_query(self, id_, **kwargs):
        return self.queries.query(id_=id_, **kwargs)

    def delete_query(self, id_, **kwargs):
        return self.queries.del_query(id_=id_, **kwargs)

    def get_query_answers(self, id_, **kwargs):
        return self.queries.query(id_=id_, **kwargs)

    def get_query_answers_content(self, id_, index, **kwargs):
        return self.queries.answers_content(id_=id_, index=index, **kwargs)

    def post_query_answers_retrieve(self, id_, index, **kwargs):
        return self.queries.answers_retrieve(id_=id_, index=index, **kwargs)

    def get_query_level(self, id_, **kwargs):
        return self.queries.level(id_=id_, **kwargs)

    def get_query_modality(self, id_, **kwargs):
        return self.queries.modality(id_=id_, **kwargs)

    def get_query_query(self, id_, **kwargs):
        return self.queries.query_query(id_=id_, **kwargs)

    def post_query_retrieve(self, id_, **kwargs):
        return self.queries.retrieve(id_=id_, **kwargs)

    #### SERIES
    def get_series(self, expand=False, since=None, limit=None, params=None, **kwargs):
        """Return series record(s).

        Use ``expand`` keyword argument to retrieve extensive information.
        Use ``since`` and ``limit`` keyword arguments to specify a group of records.

        :param bool expand:
            Return verbose information about series. Default ``False``.
            By default, returns UUIDs.
        :param int since:
            Return since nth series record. Optional. Must use with ``limit``.
        :param int limit:
            Limit to given number of records. Optional. Must use with ``since``.
        :param dict params:
            Provide overriding parameter dictionary
        :return:
            A list of records: either UUIDs or dictionary of information
        :rtype:
            list
        """
        kwargs["params"] = self.build_root_parameters(expand, since, limit, params)
        return self.series.series(**kwargs)

    def get_one_series(self, id_, **kwargs):
        return self.series.part(id_=id_, **kwargs)

    def delete_series(self, id_, **kwargs):
        return self.series.del_part(id_=id_, **kwargs)

    def anonymize_series(self, id_, data={}, **kwargs):
        return self.series.anonymize(id_=id_, json=data, **kwargs)

    def get_series_archive(self, id_, **kwargs):
        """Create a ZIP archive for media storage with DICOMDIR

        :param str id_:
            Series UUID
        :return:
            Returns zip archive as a generator
        :rtype:
            generator
        """
        return self.series.archive(id_=id_, **kwargs)

    def get_series_instances(self, id_, **kwargs):
        """Retrieve all the instances of this series in a single REST call

        :param str id_:
            Series UUID
        :return:
            Expanded information of all the instances in this series
        :rtype:
            list (dict)
        """
        return self.series.instances(id_=id_, **kwargs)

    def get_series_instances_tags(self, id_, **kwargs):
        return self.series.instances_tags(id_=id_, **kwargs)

    def get_series_media(self, id_, **kwargs):
        return self.series.media(id_=id_, **kwargs)

    def modify_series(self, id_, data, **kwargs):
        return self.series.modify(id_=id_, json=data, **kwargs)

    def get_series_module(self, id_, **kwargs):
        return self.series.module(id_=id_, **kwargs)

    def get_series_ordered_slices(self, id_, **kwargs):
        return self.series.ordered_slices(id_=id_, **kwargs)

    def get_series_patient(self, id_, **kwargs):
        return self.series.patient(id_=id_, **kwargs)

    def reconstruct_series(self, id_, **kwargs):
        return self.series.reconstruct(id_=id_, **kwargs)

    def get_series_shared_tags(self, id_, **kwargs):
        return self.series.shared_tags(id_=id_, **kwargs)

    def get_series_statistics(self, id_, **kwargs):
        return self.series.statistics(id_=id_, **kwargs)

    def get_series_study(self, id_, **kwargs):
        return self.series.study(id_=id_, **kwargs)

    #### STUDIES
    def get_studies(self, expand=False, since=None, limit=None, params=None, **kwargs):
        """Return study record(s)

        Use ``expand`` keyword argument to retrieve expanded information.
        Use ``since`` and ``limit`` keyword arguments to specify group of records.

        :param bool expand:
            Return verbose information about studies. Default ``False``.
            By default, returns UUIDs.
        :param int since:
            Return since nth study record. Optional. Must use with ``limit``.
        :param int limit:
            Limit to given number of records. Optional. Must use with ``since``.
        :param dict params:
            Provide paramaters dict to override other values
        :return:
            A list of records: either UUIDs or dictionary of information
        :rtype:
            list
        """
        kwargs["params"] = self.build_root_parameters(expand, since, limit, params)
        return self.studies.studies(**kwargs)

    def get_study(self, id_, **kwargs):
        return self.studies.study(id_=id_, **kwargs)

    def delete_study(self, id_, **kwargs):
        return self.studies.del_study(id_=id_, **kwargs)

    def anonymize_study(self, id_, data={}, **kwargs):
        return self.studies.anonymize(id_=id_, json=data, **kwargs)

    def get_study_archive(self, id_, **kwargs):
        return self.studies.archive(id_=id_, **kwargs)

    def get_study_instances(self, id_, **kwargs):
        return self.studies.instances(id_=id_, **kwargs)

    def get_study_instances_tags(self, id_, **kwargs):
        return self.studies.instances_tags(id_=id_, **kwargs)

    def get_study_media(self, id_, **kwargs):
        return self.studies.media(id_=id_, **kwargs)

    def modify_study(self, id_, data, **kwargs):
        return self.studies.modify(id_=id_, json=data, **kwargs)

    def get_study_module(self, id_, **kwargs):
        return self.studies.module(id_=id_, **kwargs)

    def get_study_module_patient(self, id_, **kwargs):
        return self.studies.module_patient(id_=id_, **kwargs)

    def get_study_patient(self, id_, **kwargs):
        return self.studies.patient(id_=id_, **kwargs)

    def reconstruct_study(self, id_, **kwargs):
        return self.studies.reconstruct(id_=id_, **kwargs)

    def get_study_series(self, id_, **kwargs):
        return self.studies.series(id_=id_, **kwargs)

    def get_study_shared_tags(self, id_, **kwargs):
        return self.studies.shared_tags(id_=id_, **kwargs)

    def get_study_statistics(self, id_, **kwargs):
        return self.studies.statistics(id_=id_, **kwargs)

    #### MODALITIES ###
    def get_modalities(self, **kwargs):
        return self.modalities.modalities(**kwargs)

    def get_modality(self, dicom, **kwargs):
        return self.modalities.modality(dicom=dicom, **kwargs)

    def delete_modality(self, dicom, **kwargs):
        return self.modalities.del_modality(dicom=dicom, **kwargs)

    def update_modality(self, dicom, data, **kwargs):
        return self.modalities.put_modality(dicom=dicom, json=data, **kwargs)

    def echo_modality(self, dicom, **kwargs):
        return self.modalities.echo(dicom=dicom, data={}, **kwargs)

    def move_modality(self, dicom, data, **kwargs):
        return self.modalities.move(dicom=dicom, json=data, **kwargs)

    def query_modality(self, dicom, data, **kwargs):
        return self.modalities.query(dicom=dicom, json=data, **kwargs)

    def store_modality(self, dicom, data, **kwargs):
        return self.modalities.store(dicom=dicom, json=data, **kwargs)

    #### SERVER-RELATED
    def get_changes(self, since=0, limit=100, last=False, **kwargs):
        """Get changes.

        Use since and limit to specify a group of records.
        Use last to get last record.

        :param int since:
            Get the records since nth record. Default ``0``
        :param int limit:
            Return given number of records. Server maximum exists at ``100`` (?). Default ``100``
        :param bool last:
            Only return most recent change. Default ``False``
        :return:
            Returns a dictionary with keys:
                'Changes': [..] # List of changes
                'Done': bool    # At most recent change?
                'Last': int     # Most recent change index returned in 'Changes'
        :rtype:
            dict
        """
        if last:
            kwargs["params"] = {"last": ""}  # overrule
        else:
            kwargs["params"] = {"since": since, "limit": limit}  # overrule
        return self.server.changes(**kwargs)

    def clear_changes(self, **kwargs):
        return self.server.del_changes(**kwargs)

    def get_exports(self, **kwargs):
        return self.server.exports(**kwargs)

    def clear_exports(self, **kwargs):
        return self.server.del_exports(**kwargs)

    def get_jobs(self, **kwargs):
        return self.server.jobs(**kwargs)

    def get_job(self, id_, **kwargs):
        return self.server.job(id_=id_, **kwargs)

    def cancel_job(self, id_, **kwargs):
        return self.server.cancel_job(id_=id_, data={}, **kwargs)

    def pause_job(self, id_, **kwargs):
        return self.server.pause_job(id_=id_, data={}, **kwargs)

    def resubmit_job(self, id_, **kwargs):
        return self.server.resubmit_job(id_=id_, data={}, **kwargs)

    def resume_job(self, id_, **kwargs):
        return self.server.resume_job(id_=id_, data={}, **kwargs)

    def get_peers(self, **kwargs):
        return self.server.peers(**kwargs)

    def get_peer(self, peer, **kwargs):
        return self.server.peer(peer=peer, **kwargs)

    def delete_peer(self, peer, **kwargs):
        return self.server.del_peer(peer=peer, **kwargs)

    def put_peer(self, peer, **kwargs):
        return self.server.put_peer(peer=peer, **kwargs)

    def store_peer(self, peer, **kwargs):
        return self.server.store_peer(peer=peer, **kwargs)

    def get_plugins(self, **kwargs):
        return self.server.plugins(**kwargs)

    def get_plugin(self, id_, **kwargs):
        return self.server.plugin(id_=id_, **kwargs)

    def get_plugins_js(self, **kwargs):
        return self.server.plugins_js(**kwargs)

    def get_statistics(self, **kwargs):
        return self.server.statistics(**kwargs)

    def get_system(self, **kwargs):
        """Get running system information

        :return:
            System information
        :rtype:
            dict
        """
        return self.server.system(**kwargs)

    def create_archive(self, **kwargs):
        return self.server.tools_create_archive(**kwargs)

    def create_dicom(self, **kwargs):
        return self.server.tools_create_dicom(**kwargs)

    def create_media(self, **kwargs):
        return self.server.tools_create_media(**kwargs)

    def create_media_extended(self, **kwargs):
        return self.server.tools_create_media_extended(**kwargs)

    def get_default_encoding(self, **kwargs):
        return self.server.tools_default_encoding(**kwargs)

    def change_default_encoding(self, **kwargs):
        return self.server.tools_post_default_encoding(**kwargs)

    def get_dicom_conformance(self, **kwargs):
        """Get the DICOM conformance statement of this version of Orthanc

        :return:
            DICOM conformance statement
        :rtype:
            str
        """
        return self.server.tools_dicom_conformance(**kwargs)

    def execute_script(self, script, **kwargs):
        return self.server.tools_execute_script(json=data, **kwargs)

    def find(self, query, level, expand=False, limit=None, **kwargs):
        """Search for matching items

        Example:

            >>> orthanc = Orthanc('https://orthanc.example.com')
            >>> query = {'PatientName': 'John*'}
            >>> orthanc.find(query, "Patient", False, 3) #returns the UUIDs of matching records

        :param dict query:
            Query to run
        :param str level:
            "Patient", "Study", "Series", or "Instance"
        :param bool expand:
            Return resources not just UUIDs (default: False)
        :param int limit:
            Limit number of records returned
        :return:
            Matching records
        :rtype:
            list
        """
        body = {"Query": query, "Level": level, "Expand": expand, "Limit": limit}
        return self.server.tools_find(json=body, **kwargs)

    def generate_uid(self, level, **kwargs):
        """Generate DICOM UID

        :param str level:
            DICOM UID level (patient, series, study, or instance)
        :return:
            UID
        :rtype:
            str
        """
        if level not in ["patient", "instance", "series", "study"]:
            raise ValueError("Must be patient, instance, series, or study")
        params = {"level": level}
        return self.server.tools_generate_uid(params=params, **kwargs)

    def invalidate_tags(self, **kwargs):
        return self.server.tools_invalidate_tags(**kwargs)

    def lookup(self, lookup, **kwargs):
        """Map DICOM UIDs to Orthanc identifiers

        :param list lookup:
            UID(s) to map
        :return:
            Orthanc identifiers
        :rtype:
            list
        """
        return self.server.tools_lookup(json=lookup, **kwargs)

    def get_now(self, **kwargs):
        """Get the current universal datetime (UTC) in the ISO 8601 format

        :return:
            Universal datetime (UTC)
        :rtype:
            str (ISO 8601)
        """
        return self.server.tools_now(**kwargs)

    def get_now_local(self, **kwargs):
        """Get the current local datetime in the ISO 8601 format

        :return:
            Local datetime
        :rtype:
            str (ISO 8601)
        """
        return self.server.tools_now_local(**kwargs)

    def reconstruct(self, **kwargs):
        """Reconstruct the main DICOM tags, JSON summary, and metadata of all instances. Slow!

        :return:
            Empty string on success or raises Exception
        :rtype:
            str
        """
        return self.server.tools_reconstruct(data={}, **kwargs)

    def reset(self, **kwargs):
        """Hot restart of Orthanc server and re-reads configuration file

        :return:
            Empty dict on success or raises Exception
        :rtype:
            dict
        """
        return self.server.tools_reset(data={}, **kwargs)

    def shutdown(self, **kwargs):
        """Stop Orthanc server

        :return:
            Empty list on success
        :rtype:
            dict
        """
        return self.server.tools_shutdown(data={}, **kwargs)
