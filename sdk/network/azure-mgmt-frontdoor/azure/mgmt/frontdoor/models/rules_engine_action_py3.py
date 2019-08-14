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


class RulesEngineAction(Model):
    """One or more actions that will execute, modifying the request and/or
    response.

    :param request_header_actions: A list of header actions to apply from the
     request from AFD to the origin.
    :type request_header_actions:
     list[~azure.mgmt.frontdoor.models.HeaderAction]
    :param response_header_actions: A list of header actions to apply from the
     response from AFD to the client.
    :type response_header_actions:
     list[~azure.mgmt.frontdoor.models.HeaderAction]
    :param route_configuration_override: Override the route configuration.
    :type route_configuration_override:
     ~azure.mgmt.frontdoor.models.RouteConfiguration
    """

    _attribute_map = {
        'request_header_actions': {'key': 'requestHeaderActions', 'type': '[HeaderAction]'},
        'response_header_actions': {'key': 'responseHeaderActions', 'type': '[HeaderAction]'},
        'route_configuration_override': {'key': 'routeConfigurationOverride', 'type': 'RouteConfiguration'},
    }

    def __init__(self, *, request_header_actions=None, response_header_actions=None, route_configuration_override=None, **kwargs) -> None:
        super(RulesEngineAction, self).__init__(**kwargs)
        self.request_header_actions = request_header_actions
        self.response_header_actions = response_header_actions
        self.route_configuration_override = route_configuration_override