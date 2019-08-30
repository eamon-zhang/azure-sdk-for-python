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


class PipelineRunInvokedBy(Model):
    """Provides entity name and id that started the pipeline run.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: Name of the entity that started the pipeline run.
    :vartype name: str
    :ivar id: The ID of the entity that started the run.
    :vartype id: str
    :ivar invoked_by_type: The type of the entity that started the run.
    :vartype invoked_by_type: str
    """

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
        'invoked_by_type': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'invoked_by_type': {'key': 'invokedByType', 'type': 'str'},
    }

    def __init__(self):
        super(PipelineRunInvokedBy, self).__init__()
        self.name = None
        self.id = None
        self.invoked_by_type = None
