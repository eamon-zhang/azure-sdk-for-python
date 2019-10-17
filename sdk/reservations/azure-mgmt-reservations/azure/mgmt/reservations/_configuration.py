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
from msrestazure import AzureConfiguration

from .version import VERSION


class MicrosoftCapacityConfiguration(AzureConfiguration):
    """Configuration for MicrosoftCapacity
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param resource_name: The Resource name for the specific resource
     provider, such as SKU name for Microsoft.Compute, pool for
     Microsoft.Batch.
    :type resource_name: str
    :param id: Quota Request id.
    :type id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, resource_name, id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if resource_name is None:
            raise ValueError("Parameter 'resource_name' must not be None.")
        if id is None:
            raise ValueError("Parameter 'id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(MicrosoftCapacityConfiguration, self).__init__(base_url)

        # Starting Autorest.Python 4.0.64, make connection pool activated by default
        self.keep_alive = True

        self.add_user_agent('azure-mgmt-reservations/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.resource_name = resource_name
        self.id = id
