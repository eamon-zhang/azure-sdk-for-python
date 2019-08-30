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

from .copy_source import CopySource


class RestSource(CopySource):
    """A copy activity Rest service source.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param source_retry_count: Source retry count. Type: integer (or
     Expression with resultType integer).
    :type source_retry_count: object
    :param source_retry_wait: Source retry wait. Type: string (or Expression
     with resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type source_retry_wait: object
    :param max_concurrent_connections: The maximum concurrent connection count
     for the source data store. Type: integer (or Expression with resultType
     integer).
    :type max_concurrent_connections: object
    :param type: Constant filled by server.
    :type type: str
    :param request_method: The HTTP method used to call the RESTful API. The
     default is GET. Type: string (or Expression with resultType string).
    :type request_method: object
    :param request_body: The HTTP request body to the RESTful API if
     requestMethod is POST. Type: string (or Expression with resultType
     string).
    :type request_body: object
    :param additional_headers: The additional HTTP headers in the request to
     the RESTful API. Type: string (or Expression with resultType string).
    :type additional_headers: object
    :param pagination_rules: The pagination rules to compose next page
     requests. Type: string (or Expression with resultType string).
    :type pagination_rules: object
    :param http_request_timeout: The timeout (TimeSpan) to get an HTTP
     response. It is the timeout to get a response, not the timeout to read
     response data. Default value: 00:01:40. Type: string (or Expression with
     resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type http_request_timeout: object
    :param request_interval: The time to await before sending next page
     request.
    :type request_interval: object
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'source_retry_count': {'key': 'sourceRetryCount', 'type': 'object'},
        'source_retry_wait': {'key': 'sourceRetryWait', 'type': 'object'},
        'max_concurrent_connections': {'key': 'maxConcurrentConnections', 'type': 'object'},
        'type': {'key': 'type', 'type': 'str'},
        'request_method': {'key': 'requestMethod', 'type': 'object'},
        'request_body': {'key': 'requestBody', 'type': 'object'},
        'additional_headers': {'key': 'additionalHeaders', 'type': 'object'},
        'pagination_rules': {'key': 'paginationRules', 'type': 'object'},
        'http_request_timeout': {'key': 'httpRequestTimeout', 'type': 'object'},
        'request_interval': {'key': 'requestInterval', 'type': 'object'},
    }

    def __init__(self, additional_properties=None, source_retry_count=None, source_retry_wait=None, max_concurrent_connections=None, request_method=None, request_body=None, additional_headers=None, pagination_rules=None, http_request_timeout=None, request_interval=None):
        super(RestSource, self).__init__(additional_properties=additional_properties, source_retry_count=source_retry_count, source_retry_wait=source_retry_wait, max_concurrent_connections=max_concurrent_connections)
        self.request_method = request_method
        self.request_body = request_body
        self.additional_headers = additional_headers
        self.pagination_rules = pagination_rules
        self.http_request_timeout = http_request_timeout
        self.request_interval = request_interval
        self.type = 'RestSource'
