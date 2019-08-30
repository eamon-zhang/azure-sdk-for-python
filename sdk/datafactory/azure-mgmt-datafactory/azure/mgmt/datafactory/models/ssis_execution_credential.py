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


class SSISExecutionCredential(Model):
    """SSIS package execution credential.

    :param domain: Domain for windows authentication.
    :type domain: object
    :param user_name: UseName for windows authentication.
    :type user_name: object
    :param password: Password for windows authentication.
    :type password: ~azure.mgmt.datafactory.models.SecureString
    """

    _validation = {
        'domain': {'required': True},
        'user_name': {'required': True},
        'password': {'required': True},
    }

    _attribute_map = {
        'domain': {'key': 'domain', 'type': 'object'},
        'user_name': {'key': 'userName', 'type': 'object'},
        'password': {'key': 'password', 'type': 'SecureString'},
    }

    def __init__(self, domain, user_name, password):
        super(SSISExecutionCredential, self).__init__()
        self.domain = domain
        self.user_name = user_name
        self.password = password
