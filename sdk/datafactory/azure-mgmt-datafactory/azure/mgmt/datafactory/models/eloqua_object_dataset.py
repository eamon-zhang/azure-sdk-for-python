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

from .dataset import Dataset


class EloquaObjectDataset(Dataset):
    """Eloqua server dataset.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param description: Dataset description.
    :type description: str
    :param structure: Columns that define the structure of the dataset. Type:
     array (or Expression with resultType array), itemType: DatasetDataElement.
    :type structure: object
    :param schema: Columns that define the physical type schema of the
     dataset. Type: array (or Expression with resultType array), itemType:
     DatasetSchemaDataElement.
    :type schema: object
    :param linked_service_name: Linked service reference.
    :type linked_service_name:
     ~azure.mgmt.datafactory.models.LinkedServiceReference
    :param parameters: Parameters for dataset.
    :type parameters: dict[str,
     ~azure.mgmt.datafactory.models.ParameterSpecification]
    :param annotations: List of tags that can be used for describing the
     Dataset.
    :type annotations: list[object]
    :param folder: The folder that this Dataset is in. If not specified,
     Dataset will appear at the root level.
    :type folder: ~azure.mgmt.datafactory.models.DatasetFolder
    :param type: Constant filled by server.
    :type type: str
    :param table_name: The table name. Type: string (or Expression with
     resultType string).
    :type table_name: object
    """

    _validation = {
        'linked_service_name': {'required': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'description': {'key': 'description', 'type': 'str'},
        'structure': {'key': 'structure', 'type': 'object'},
        'schema': {'key': 'schema', 'type': 'object'},
        'linked_service_name': {'key': 'linkedServiceName', 'type': 'LinkedServiceReference'},
        'parameters': {'key': 'parameters', 'type': '{ParameterSpecification}'},
        'annotations': {'key': 'annotations', 'type': '[object]'},
        'folder': {'key': 'folder', 'type': 'DatasetFolder'},
        'type': {'key': 'type', 'type': 'str'},
        'table_name': {'key': 'typeProperties.tableName', 'type': 'object'},
    }

    def __init__(self, linked_service_name, additional_properties=None, description=None, structure=None, schema=None, parameters=None, annotations=None, folder=None, table_name=None):
        super(EloquaObjectDataset, self).__init__(additional_properties=additional_properties, description=description, structure=structure, schema=schema, linked_service_name=linked_service_name, parameters=parameters, annotations=annotations, folder=folder)
        self.table_name = table_name
        self.type = 'EloquaObject'
