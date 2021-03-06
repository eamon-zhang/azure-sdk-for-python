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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import RedisManagementClientConfiguration
from .operations import Operations
from .operations import RedisOperations
from .operations import FirewallRulesOperations
from .operations import PatchSchedulesOperations
from .operations import LinkedServerOperations
from . import models


class RedisManagementClient(SDKClient):
    """REST API for Azure Redis Cache Service.

    :ivar config: Configuration for client.
    :vartype config: RedisManagementClientConfiguration

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.redis.operations.Operations
    :ivar redis: Redis operations
    :vartype redis: azure.mgmt.redis.operations.RedisOperations
    :ivar firewall_rules: FirewallRules operations
    :vartype firewall_rules: azure.mgmt.redis.operations.FirewallRulesOperations
    :ivar patch_schedules: PatchSchedules operations
    :vartype patch_schedules: azure.mgmt.redis.operations.PatchSchedulesOperations
    :ivar linked_server: LinkedServer operations
    :vartype linked_server: azure.mgmt.redis.operations.LinkedServerOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Gets subscription credentials which uniquely
     identify the Microsoft Azure subscription. The subscription ID forms part
     of the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = RedisManagementClientConfiguration(credentials, subscription_id, base_url)
        super(RedisManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2019-07-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.redis = RedisOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.firewall_rules = FirewallRulesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.patch_schedules = PatchSchedulesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.linked_server = LinkedServerOperations(
            self._client, self.config, self._serialize, self._deserialize)
