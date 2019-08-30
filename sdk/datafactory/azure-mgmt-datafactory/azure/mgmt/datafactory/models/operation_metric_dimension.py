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


class OperationMetricDimension(Model):
    """Defines the metric dimension.

    :param name: The name of the dimension for the metric.
    :type name: str
    :param display_name: The display name of the metric dimension.
    :type display_name: str
    :param to_be_exported_for_shoebox: Whether the dimension should be
     exported to Azure Monitor.
    :type to_be_exported_for_shoebox: bool
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'to_be_exported_for_shoebox': {'key': 'toBeExportedForShoebox', 'type': 'bool'},
    }

    def __init__(self, name=None, display_name=None, to_be_exported_for_shoebox=None):
        super(OperationMetricDimension, self).__init__()
        self.name = name
        self.display_name = display_name
        self.to_be_exported_for_shoebox = to_be_exported_for_shoebox
