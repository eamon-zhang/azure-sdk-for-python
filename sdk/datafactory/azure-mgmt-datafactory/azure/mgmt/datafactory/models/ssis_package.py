# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .ssis_object_metadata import SsisObjectMetadata


class SsisPackage(SsisObjectMetadata):
    """Ssis Package.

    :param id: Metadata id.
    :type id: long
    :param name: Metadata name.
    :type name: str
    :param description: Metadata description.
    :type description: str
    :param type: Constant filled by server.
    :type type: str
    :param folder_id: Folder id which contains package.
    :type folder_id: long
    :param project_version: Project version which contains package.
    :type project_version: long
    :param project_id: Project id which contains package.
    :type project_id: long
    :param parameters: Parameters in package
    :type parameters: list[~azure.mgmt.datafactory.models.SsisParameter]
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'long'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'folder_id': {'key': 'folderId', 'type': 'long'},
        'project_version': {'key': 'projectVersion', 'type': 'long'},
        'project_id': {'key': 'projectId', 'type': 'long'},
        'parameters': {'key': 'parameters', 'type': '[SsisParameter]'},
    }

    def __init__(self, id=None, name=None, description=None, folder_id=None, project_version=None, project_id=None, parameters=None):
        super(SsisPackage, self).__init__(id=id, name=name, description=description)
        self.folder_id = folder_id
        self.project_version = project_version
        self.project_id = project_id
        self.parameters = parameters
        self.type = 'Package'
