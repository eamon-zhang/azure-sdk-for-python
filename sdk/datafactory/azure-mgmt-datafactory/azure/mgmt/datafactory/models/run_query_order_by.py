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


class RunQueryOrderBy(Model):
    """An object to provide order by options for listing runs.

    :param order_by: Parameter name to be used for order by. The allowed
     parameters to order by for pipeline runs are PipelineName, RunStart,
     RunEnd and Status; for activity runs are ActivityName, ActivityRunStart,
     ActivityRunEnd and Status; for trigger runs are TriggerName,
     TriggerRunTimestamp and Status. Possible values include: 'RunStart',
     'RunEnd', 'PipelineName', 'Status', 'ActivityName', 'ActivityRunStart',
     'ActivityRunEnd', 'TriggerName', 'TriggerRunTimestamp'
    :type order_by: str or ~azure.mgmt.datafactory.models.RunQueryOrderByField
    :param order: Sorting order of the parameter. Possible values include:
     'ASC', 'DESC'
    :type order: str or ~azure.mgmt.datafactory.models.RunQueryOrder
    """

    _validation = {
        'order_by': {'required': True},
        'order': {'required': True},
    }

    _attribute_map = {
        'order_by': {'key': 'orderBy', 'type': 'str'},
        'order': {'key': 'order', 'type': 'str'},
    }

    def __init__(self, order_by, order):
        super(RunQueryOrderBy, self).__init__()
        self.order_by = order_by
        self.order = order
