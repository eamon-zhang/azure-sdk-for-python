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


class EndpointDependency(Model):
    """A domain name that a service is reached at, including details of the
    current connection status.

    :param domain_name: The domain name of the dependency.
    :type domain_name: str
    :param endpoint_details: The IP Addresses and Ports used when connecting
     to DomainName.
    :type endpoint_details: list[~azure.mgmt.web.models.EndpointDetail]
    """

    _attribute_map = {
        'domain_name': {'key': 'domainName', 'type': 'str'},
        'endpoint_details': {'key': 'endpointDetails', 'type': '[EndpointDetail]'},
    }

    def __init__(self, **kwargs):
        super(EndpointDependency, self).__init__(**kwargs)
        self.domain_name = kwargs.get('domain_name', None)
        self.endpoint_details = kwargs.get('endpoint_details', None)