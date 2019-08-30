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


class ActivityRunsQueryResponse(Model):
    """A list activity runs.

    :param value: List of activity runs.
    :type value: list[~azure.mgmt.datafactory.models.ActivityRun]
    :param continuation_token: The continuation token for getting the next
     page of results, if any remaining results exist, null otherwise.
    :type continuation_token: str
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ActivityRun]'},
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
    }

    def __init__(self, value, continuation_token=None):
        super(ActivityRunsQueryResponse, self).__init__()
        self.value = value
        self.continuation_token = continuation_token
