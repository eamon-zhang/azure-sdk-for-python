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

from msrest.serialization import Model


class IoTSecuritySolutionModel(Model):
    """Security Solution.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param location: The resource location.
    :type location: str
    :param workspace: Required. Workspace resource ID
    :type workspace: str
    :param display_name: Required. Resource display name.
    :type display_name: str
    :param status: Security solution status. Possible values include:
     'Enabled', 'Disabled'. Default value: "Enabled" .
    :type status: str or ~azure.mgmt.security.models.SecuritySolutionStatus
    :param export: List of additional export to workspace data options
    :type export: list[str or ~azure.mgmt.security.models.ExportData]
    :param disabled_data_sources: Disabled data sources. Disabling these data
     sources compromises the system.
    :type disabled_data_sources: list[str or
     ~azure.mgmt.security.models.DataSource]
    :param iot_hubs: Required. IoT Hub resource IDs
    :type iot_hubs: list[str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'workspace': {'required': True},
        'display_name': {'required': True},
        'iot_hubs': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'workspace': {'key': 'properties.workspace', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'export': {'key': 'properties.export', 'type': '[str]'},
        'disabled_data_sources': {'key': 'properties.disabledDataSources', 'type': '[str]'},
        'iot_hubs': {'key': 'properties.iotHubs', 'type': '[str]'},
    }

    def __init__(self, *, workspace: str, display_name: str, iot_hubs, tags=None, location: str=None, status="Enabled", export=None, disabled_data_sources=None, **kwargs) -> None:
        super(IoTSecuritySolutionModel, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.tags = tags
        self.location = location
        self.workspace = workspace
        self.display_name = display_name
        self.status = status
        self.export = export
        self.disabled_data_sources = disabled_data_sources
        self.iot_hubs = iot_hubs