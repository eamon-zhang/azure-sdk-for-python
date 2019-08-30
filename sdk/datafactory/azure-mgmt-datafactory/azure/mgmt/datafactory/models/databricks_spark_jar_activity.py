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

from .execution_activity import ExecutionActivity


class DatabricksSparkJarActivity(ExecutionActivity):
    """DatabricksSparkJar activity.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param name: Activity name.
    :type name: str
    :param description: Activity description.
    :type description: str
    :param depends_on: Activity depends on condition.
    :type depends_on: list[~azure.mgmt.datafactory.models.ActivityDependency]
    :param user_properties: Activity user properties.
    :type user_properties: list[~azure.mgmt.datafactory.models.UserProperty]
    :param type: Constant filled by server.
    :type type: str
    :param linked_service_name: Linked service reference.
    :type linked_service_name:
     ~azure.mgmt.datafactory.models.LinkedServiceReference
    :param policy: Activity policy.
    :type policy: ~azure.mgmt.datafactory.models.ActivityPolicy
    :param main_class_name: The full name of the class containing the main
     method to be executed. This class must be contained in a JAR provided as a
     library. Type: string (or Expression with resultType string).
    :type main_class_name: object
    :param parameters: Parameters that will be passed to the main method.
    :type parameters: list[object]
    :param libraries: A list of libraries to be installed on the cluster that
     will execute the job.
    :type libraries: list[dict[str, object]]
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
        'main_class_name': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'depends_on': {'key': 'dependsOn', 'type': '[ActivityDependency]'},
        'user_properties': {'key': 'userProperties', 'type': '[UserProperty]'},
        'type': {'key': 'type', 'type': 'str'},
        'linked_service_name': {'key': 'linkedServiceName', 'type': 'LinkedServiceReference'},
        'policy': {'key': 'policy', 'type': 'ActivityPolicy'},
        'main_class_name': {'key': 'typeProperties.mainClassName', 'type': 'object'},
        'parameters': {'key': 'typeProperties.parameters', 'type': '[object]'},
        'libraries': {'key': 'typeProperties.libraries', 'type': '[{object}]'},
    }

    def __init__(self, name, main_class_name, additional_properties=None, description=None, depends_on=None, user_properties=None, linked_service_name=None, policy=None, parameters=None, libraries=None):
        super(DatabricksSparkJarActivity, self).__init__(additional_properties=additional_properties, name=name, description=description, depends_on=depends_on, user_properties=user_properties, linked_service_name=linked_service_name, policy=policy)
        self.main_class_name = main_class_name
        self.parameters = parameters
        self.libraries = libraries
        self.type = 'DatabricksSparkJar'
