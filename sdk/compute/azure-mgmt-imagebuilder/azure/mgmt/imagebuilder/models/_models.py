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
from msrest.exceptions import HttpOperationError


class ApiError(Model):
    """Api error.

    :param details: The Api error details
    :type details: list[~azure.mgmt.imagebuilder.models.ApiErrorBase]
    :param inner_error: The Api inner error
    :type inner_error: ~azure.mgmt.imagebuilder.models.InnerError
    :param code: The error code.
    :type code: str
    :param target: The target of the particular error.
    :type target: str
    :param message: The error message.
    :type message: str
    """

    _attribute_map = {
        'details': {'key': 'details', 'type': '[ApiErrorBase]'},
        'inner_error': {'key': 'innerError', 'type': 'InnerError'},
        'code': {'key': 'code', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ApiError, self).__init__(**kwargs)
        self.details = kwargs.get('details', None)
        self.inner_error = kwargs.get('inner_error', None)
        self.code = kwargs.get('code', None)
        self.target = kwargs.get('target', None)
        self.message = kwargs.get('message', None)


class ApiErrorException(HttpOperationError):
    """Server responsed with exception of type: 'ApiError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ApiErrorException, self).__init__(deserialize, response, 'ApiError', *args)


class ApiErrorBase(Model):
    """Api error base.

    :param code: The error code.
    :type code: str
    :param target: The target of the particular error.
    :type target: str
    :param message: The error message.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ApiErrorBase, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.target = kwargs.get('target', None)
        self.message = kwargs.get('message', None)


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class Resource(Model):
    """The Resource model definition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = kwargs.get('location', None)
        self.tags = kwargs.get('tags', None)


class ImageTemplate(Resource):
    """Image template is an ARM resource managed by Microsoft.VirtualMachineImages
    provider.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param source: Required. Specifies the properties used to describe the
     source image.
    :type source: ~azure.mgmt.imagebuilder.models.ImageTemplateSource
    :param customize: Specifies the properties used to describe the
     customization steps of the image, like Image source etc
    :type customize:
     list[~azure.mgmt.imagebuilder.models.ImageTemplateCustomizer]
    :param distribute: Required. The distribution targets where the image
     output needs to go to.
    :type distribute:
     list[~azure.mgmt.imagebuilder.models.ImageTemplateDistributor]
    :ivar provisioning_state: Provisioning state of the resource. Possible
     values include: 'Creating', 'Updating', 'Succeeded', 'Failed', 'Deleting'
    :vartype provisioning_state: str or
     ~azure.mgmt.imagebuilder.models.ProvisioningState
    :ivar provisioning_error: Provisioning error, if any
    :vartype provisioning_error:
     ~azure.mgmt.imagebuilder.models.ProvisioningError
    :ivar last_run_status: State of 'run' that is currently executing or was
     last executed.
    :vartype last_run_status:
     ~azure.mgmt.imagebuilder.models.ImageTemplateLastRunStatus
    :param build_timeout_in_minutes: Maximum duration to wait while building
     the image template. Omit or specify 0 to use the default (4 hours).
    :type build_timeout_in_minutes: int
    :param vm_profile: Describes how virtual machine is set up to build images
    :type vm_profile: ~azure.mgmt.imagebuilder.models.ImageTemplateVmProfile
    :param identity: The identity of the image template, if configured.
    :type identity: ~azure.mgmt.imagebuilder.models.ImageTemplateIdentity
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'source': {'required': True},
        'distribute': {'required': True},
        'provisioning_state': {'readonly': True},
        'provisioning_error': {'readonly': True},
        'last_run_status': {'readonly': True},
        'build_timeout_in_minutes': {'maximum': 960, 'minimum': 0},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'source': {'key': 'properties.source', 'type': 'ImageTemplateSource'},
        'customize': {'key': 'properties.customize', 'type': '[ImageTemplateCustomizer]'},
        'distribute': {'key': 'properties.distribute', 'type': '[ImageTemplateDistributor]'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'ProvisioningState'},
        'provisioning_error': {'key': 'properties.provisioningError', 'type': 'ProvisioningError'},
        'last_run_status': {'key': 'properties.lastRunStatus', 'type': 'ImageTemplateLastRunStatus'},
        'build_timeout_in_minutes': {'key': 'properties.buildTimeoutInMinutes', 'type': 'int'},
        'vm_profile': {'key': 'properties.vmProfile', 'type': 'ImageTemplateVmProfile'},
        'identity': {'key': 'identity', 'type': 'ImageTemplateIdentity'},
    }

    def __init__(self, **kwargs):
        super(ImageTemplate, self).__init__(**kwargs)
        self.source = kwargs.get('source', None)
        self.customize = kwargs.get('customize', None)
        self.distribute = kwargs.get('distribute', None)
        self.provisioning_state = None
        self.provisioning_error = None
        self.last_run_status = None
        self.build_timeout_in_minutes = kwargs.get('build_timeout_in_minutes', None)
        self.vm_profile = kwargs.get('vm_profile', None)
        self.identity = kwargs.get('identity', None)


class ImageTemplateCustomizer(Model):
    """Describes a unit of image customization.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: ImageTemplateShellCustomizer,
    ImageTemplateRestartCustomizer, ImageTemplatePowerShellCustomizer,
    ImageTemplateFileCustomizer

    All required parameters must be populated in order to send to Azure.

    :param name: Friendly Name to provide context on what this customization
     step does
    :type name: str
    :param type: Required. Constant filled by server.
    :type type: str
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    _subtype_map = {
        'type': {'Shell': 'ImageTemplateShellCustomizer', 'WindowsRestart': 'ImageTemplateRestartCustomizer', 'PowerShell': 'ImageTemplatePowerShellCustomizer', 'File': 'ImageTemplateFileCustomizer'}
    }

    def __init__(self, **kwargs):
        super(ImageTemplateCustomizer, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.type = None


class ImageTemplateDistributor(Model):
    """Generic distribution object.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: ImageTemplateManagedImageDistributor,
    ImageTemplateSharedImageDistributor, ImageTemplateVhdDistributor

    All required parameters must be populated in order to send to Azure.

    :param run_output_name: Required. The name to be used for the associated
     RunOutput.
    :type run_output_name: str
    :param artifact_tags: Tags that will be applied to the artifact once it
     has been created/updated by the distributor.
    :type artifact_tags: dict[str, str]
    :param type: Required. Constant filled by server.
    :type type: str
    """

    _validation = {
        'run_output_name': {'required': True, 'pattern': r'^[A-Za-z0-9-_.]{1,64}$'},
        'type': {'required': True},
    }

    _attribute_map = {
        'run_output_name': {'key': 'runOutputName', 'type': 'str'},
        'artifact_tags': {'key': 'artifactTags', 'type': '{str}'},
        'type': {'key': 'type', 'type': 'str'},
    }

    _subtype_map = {
        'type': {'ManagedImage': 'ImageTemplateManagedImageDistributor', 'SharedImage': 'ImageTemplateSharedImageDistributor', 'VHD': 'ImageTemplateVhdDistributor'}
    }

    def __init__(self, **kwargs):
        super(ImageTemplateDistributor, self).__init__(**kwargs)
        self.run_output_name = kwargs.get('run_output_name', None)
        self.artifact_tags = kwargs.get('artifact_tags', None)
        self.type = None


class ImageTemplateFileCustomizer(ImageTemplateCustomizer):
    """Uploads files to VMs (Linux, Windows). Corresponds to Packer file
    provisioner.

    All required parameters must be populated in order to send to Azure.

    :param name: Friendly Name to provide context on what this customization
     step does
    :type name: str
    :param type: Required. Constant filled by server.
    :type type: str
    :param source_uri: The URI of the file to be uploaded for customizing the
     VM. It can be a github link, SAS URI for Azure Storage, etc
    :type source_uri: str
    :param sha256_checksum: SHA256 checksum of the file provided in the
     sourceUri field above
    :type sha256_checksum: str
    :param destination: The absolute path to a file (with nested directory
     structures already created) where the file (from sourceUri) will be
     uploaded to in the VM
    :type destination: str
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'source_uri': {'key': 'sourceUri', 'type': 'str'},
        'sha256_checksum': {'key': 'sha256Checksum', 'type': 'str'},
        'destination': {'key': 'destination', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ImageTemplateFileCustomizer, self).__init__(**kwargs)
        self.source_uri = kwargs.get('source_uri', None)
        self.sha256_checksum = kwargs.get('sha256_checksum', None)
        self.destination = kwargs.get('destination', None)
        self.type = 'File'


class ImageTemplateIdentity(Model):
    """Identity for the image template.

    :param type: The type of identity used for the image template. The type
     'None' will remove any identities from the image template. Possible values
     include: 'UserAssigned', 'None'
    :type type: str or ~azure.mgmt.imagebuilder.models.ResourceIdentityType
    :param user_assigned_identities: The list of user identities associated
     with the image template. The user identity dictionary key references will
     be ARM resource ids in the form:
     '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
    :type user_assigned_identities: dict[str,
     ~azure.mgmt.imagebuilder.models.ImageTemplateIdentityUserAssignedIdentitiesValue]
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'ResourceIdentityType'},
        'user_assigned_identities': {'key': 'userAssignedIdentities', 'type': '{ImageTemplateIdentityUserAssignedIdentitiesValue}'},
    }

    def __init__(self, **kwargs):
        super(ImageTemplateIdentity, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.user_assigned_identities = kwargs.get('user_assigned_identities', None)


class ImageTemplateIdentityUserAssignedIdentitiesValue(Model):
    """ImageTemplateIdentityUserAssignedIdentitiesValue.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar principal_id: The principal id of user assigned identity.
    :vartype principal_id: str
    :ivar client_id: The client id of user assigned identity.
    :vartype client_id: str
    """

    _validation = {
        'principal_id': {'readonly': True},
        'client_id': {'readonly': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'client_id': {'key': 'clientId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ImageTemplateIdentityUserAssignedIdentitiesValue, self).__init__(**kwargs)
        self.principal_id = None
        self.client_id = None


class ImageTemplateSource(Model):
    """Describes a virtual machine image source for building, customizing and
    distributing.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: ImageTemplateIsoSource, ImageTemplatePlatformImageSource,
    ImageTemplateManagedImageSource, ImageTemplateSharedImageVersionSource

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
    }

    _subtype_map = {
        'type': {'ISO': 'ImageTemplateIsoSource', 'PlatformImage': 'ImageTemplatePlatformImageSource', 'ManagedImage': 'ImageTemplateManagedImageSource', 'SharedImageVersion': 'ImageTemplateSharedImageVersionSource'}
    }

    def __init__(self, **kwargs):
        super(ImageTemplateSource, self).__init__(**kwargs)
        self.type = None


class ImageTemplateIsoSource(ImageTemplateSource):
    """Describes an image source that is an installation ISO. Currently only
    supports Red Hat Enterprise Linux 7.2-7.5 ISO's.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :param source_uri: Required. URI to get the ISO image. This URI has to be
     accessible to the resource provider at the time of the image template
     creation.
    :type source_uri: str
    :param sha256_checksum: Required. SHA256 Checksum of the ISO image.
    :type sha256_checksum: str
    """

    _validation = {
        'type': {'required': True},
        'source_uri': {'required': True},
        'sha256_checksum': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'source_uri': {'key': 'sourceUri', 'type': 'str'},
        'sha256_checksum': {'key': 'sha256Checksum', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ImageTemplateIsoSource, self).__init__(**kwargs)
        self.source_uri = kwargs.get('source_uri', None)
        self.sha256_checksum = kwargs.get('sha256_checksum', None)
        self.type = 'ISO'


class ImageTemplateLastRunStatus(Model):
    """Describes the latest status of running an image template.

    :param start_time: Start time of the last run (UTC)
    :type start_time: datetime
    :param end_time: End time of the last run (UTC)
    :type end_time: datetime
    :param run_state: State of the last run. Possible values include:
     'Running', 'Succeeded', 'PartiallySucceeded', 'Failed'
    :type run_state: str or ~azure.mgmt.imagebuilder.models.RunState
    :param run_sub_state: Sub-state of the last run. Possible values include:
     'Queued', 'Building', 'Customizing', 'Distributing'
    :type run_sub_state: str or ~azure.mgmt.imagebuilder.models.RunSubState
    :param message: Verbose information about the last run state
    :type message: str
    """

    _attribute_map = {
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'run_state': {'key': 'runState', 'type': 'RunState'},
        'run_sub_state': {'key': 'runSubState', 'type': 'RunSubState'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ImageTemplateLastRunStatus, self).__init__(**kwargs)
        self.start_time = kwargs.get('start_time', None)
        self.end_time = kwargs.get('end_time', None)
        self.run_state = kwargs.get('run_state', None)
        self.run_sub_state = kwargs.get('run_sub_state', None)
        self.message = kwargs.get('message', None)


class ImageTemplateManagedImageDistributor(ImageTemplateDistributor):
    """Distribute as a Managed Disk Image.

    All required parameters must be populated in order to send to Azure.

    :param run_output_name: Required. The name to be used for the associated
     RunOutput.
    :type run_output_name: str
    :param artifact_tags: Tags that will be applied to the artifact once it
     has been created/updated by the distributor.
    :type artifact_tags: dict[str, str]
    :param type: Required. Constant filled by server.
    :type type: str
    :param image_id: Required. Resource Id of the Managed Disk Image
    :type image_id: str
    :param location: Required. Azure location for the image, should match if
     image already exists
    :type location: str
    """

    _validation = {
        'run_output_name': {'required': True, 'pattern': r'^[A-Za-z0-9-_.]{1,64}$'},
        'type': {'required': True},
        'image_id': {'required': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'run_output_name': {'key': 'runOutputName', 'type': 'str'},
        'artifact_tags': {'key': 'artifactTags', 'type': '{str}'},
        'type': {'key': 'type', 'type': 'str'},
        'image_id': {'key': 'imageId', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ImageTemplateManagedImageDistributor, self).__init__(**kwargs)
        self.image_id = kwargs.get('image_id', None)
        self.location = kwargs.get('location', None)
        self.type = 'ManagedImage'


class ImageTemplateManagedImageSource(ImageTemplateSource):
    """Describes an image source that is a managed image in customer subscription.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :param image_id: Required. ARM resource id of the managed image in
     customer subscription
    :type image_id: str
    """

    _validation = {
        'type': {'required': True},
        'image_id': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'image_id': {'key': 'imageId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ImageTemplateManagedImageSource, self).__init__(**kwargs)
        self.image_id = kwargs.get('image_id', None)
        self.type = 'ManagedImage'


class ImageTemplatePlatformImageSource(ImageTemplateSource):
    """Describes an image source from [Azure Gallery
    Images](https://docs.microsoft.com/en-us/rest/api/compute/virtualmachineimages).

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :param publisher: Image Publisher in [Azure Gallery
     Images](https://docs.microsoft.com/en-us/rest/api/compute/virtualmachineimages).
    :type publisher: str
    :param offer: Image offer from the [Azure Gallery
     Images](https://docs.microsoft.com/en-us/rest/api/compute/virtualmachineimages).
    :type offer: str
    :param sku: Image sku from the [Azure Gallery
     Images](https://docs.microsoft.com/en-us/rest/api/compute/virtualmachineimages).
    :type sku: str
    :param version: Image version from the [Azure Gallery
     Images](https://docs.microsoft.com/en-us/rest/api/compute/virtualmachineimages).
    :type version: str
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'publisher': {'key': 'publisher', 'type': 'str'},
        'offer': {'key': 'offer', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ImageTemplatePlatformImageSource, self).__init__(**kwargs)
        self.publisher = kwargs.get('publisher', None)
        self.offer = kwargs.get('offer', None)
        self.sku = kwargs.get('sku', None)
        self.version = kwargs.get('version', None)
        self.type = 'PlatformImage'


class ImageTemplatePowerShellCustomizer(ImageTemplateCustomizer):
    """Runs the specified PowerShell on the VM (Windows). Corresponds to Packer
    powershell provisioner. Exactly one of 'scriptUri' or 'inline' can be
    specified.

    All required parameters must be populated in order to send to Azure.

    :param name: Friendly Name to provide context on what this customization
     step does
    :type name: str
    :param type: Required. Constant filled by server.
    :type type: str
    :param script_uri: URI of the PowerShell script to be run for customizing.
     It can be a github link, SAS URI for Azure Storage, etc
    :type script_uri: str
    :param sha256_checksum: SHA256 checksum of the power shell script provided
     in the scriptUri field above
    :type sha256_checksum: str
    :param inline: Array of PowerShell commands to execute
    :type inline: list[str]
    :param run_elevated: If specified, the PowerShell script will be run with
     elevated privileges
    :type run_elevated: bool
    :param valid_exit_codes: Valid exit codes for the PowerShell script.
     [Default: 0]
    :type valid_exit_codes: list[int]
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'script_uri': {'key': 'scriptUri', 'type': 'str'},
        'sha256_checksum': {'key': 'sha256Checksum', 'type': 'str'},
        'inline': {'key': 'inline', 'type': '[str]'},
        'run_elevated': {'key': 'runElevated', 'type': 'bool'},
        'valid_exit_codes': {'key': 'validExitCodes', 'type': '[int]'},
    }

    def __init__(self, **kwargs):
        super(ImageTemplatePowerShellCustomizer, self).__init__(**kwargs)
        self.script_uri = kwargs.get('script_uri', None)
        self.sha256_checksum = kwargs.get('sha256_checksum', None)
        self.inline = kwargs.get('inline', None)
        self.run_elevated = kwargs.get('run_elevated', None)
        self.valid_exit_codes = kwargs.get('valid_exit_codes', None)
        self.type = 'PowerShell'


class ImageTemplateRestartCustomizer(ImageTemplateCustomizer):
    """Reboots a VM and waits for it to come back online (Windows). Corresponds to
    Packer windows-restart provisioner.

    All required parameters must be populated in order to send to Azure.

    :param name: Friendly Name to provide context on what this customization
     step does
    :type name: str
    :param type: Required. Constant filled by server.
    :type type: str
    :param restart_command: Command to execute the restart [Default: 'shutdown
     /r /f /t 0 /c "packer restart"']
    :type restart_command: str
    :param restart_check_command: Command to check if restart succeeded
     [Default: '']
    :type restart_check_command: str
    :param restart_timeout: Restart timeout specified as a string of magnitude
     and unit, e.g. '5m' (5 minutes) or '2h' (2 hours) [Default: '5m']
    :type restart_timeout: str
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'restart_command': {'key': 'restartCommand', 'type': 'str'},
        'restart_check_command': {'key': 'restartCheckCommand', 'type': 'str'},
        'restart_timeout': {'key': 'restartTimeout', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ImageTemplateRestartCustomizer, self).__init__(**kwargs)
        self.restart_command = kwargs.get('restart_command', None)
        self.restart_check_command = kwargs.get('restart_check_command', None)
        self.restart_timeout = kwargs.get('restart_timeout', None)
        self.type = 'WindowsRestart'


class ImageTemplateSharedImageDistributor(ImageTemplateDistributor):
    """Distribute via Shared Image Gallery.

    All required parameters must be populated in order to send to Azure.

    :param run_output_name: Required. The name to be used for the associated
     RunOutput.
    :type run_output_name: str
    :param artifact_tags: Tags that will be applied to the artifact once it
     has been created/updated by the distributor.
    :type artifact_tags: dict[str, str]
    :param type: Required. Constant filled by server.
    :type type: str
    :param gallery_image_id: Required. Resource Id of the Shared Image Gallery
     image
    :type gallery_image_id: str
    :param replication_regions: Required. A list of regions that the image
     will be replicated to
    :type replication_regions: list[str]
    """

    _validation = {
        'run_output_name': {'required': True, 'pattern': r'^[A-Za-z0-9-_.]{1,64}$'},
        'type': {'required': True},
        'gallery_image_id': {'required': True},
        'replication_regions': {'required': True},
    }

    _attribute_map = {
        'run_output_name': {'key': 'runOutputName', 'type': 'str'},
        'artifact_tags': {'key': 'artifactTags', 'type': '{str}'},
        'type': {'key': 'type', 'type': 'str'},
        'gallery_image_id': {'key': 'galleryImageId', 'type': 'str'},
        'replication_regions': {'key': 'replicationRegions', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(ImageTemplateSharedImageDistributor, self).__init__(**kwargs)
        self.gallery_image_id = kwargs.get('gallery_image_id', None)
        self.replication_regions = kwargs.get('replication_regions', None)
        self.type = 'SharedImage'


class ImageTemplateSharedImageVersionSource(ImageTemplateSource):
    """Describes an image source that is an image version in a shared image
    gallery.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :param image_version_id: Required. ARM resource id of the image version in
     the shared image gallery
    :type image_version_id: str
    """

    _validation = {
        'type': {'required': True},
        'image_version_id': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'image_version_id': {'key': 'imageVersionId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ImageTemplateSharedImageVersionSource, self).__init__(**kwargs)
        self.image_version_id = kwargs.get('image_version_id', None)
        self.type = 'SharedImageVersion'


class ImageTemplateShellCustomizer(ImageTemplateCustomizer):
    """Runs a shell script during the customization phase (Linux). Corresponds to
    Packer shell provisioner. Exactly one of 'scriptUri' or 'inline' can be
    specified.

    All required parameters must be populated in order to send to Azure.

    :param name: Friendly Name to provide context on what this customization
     step does
    :type name: str
    :param type: Required. Constant filled by server.
    :type type: str
    :param script_uri: URI of the shell script to be run for customizing. It
     can be a github link, SAS URI for Azure Storage, etc
    :type script_uri: str
    :param sha256_checksum: SHA256 checksum of the shell script provided in
     the scriptUri field
    :type sha256_checksum: str
    :param inline: Array of shell commands to execute
    :type inline: list[str]
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'script_uri': {'key': 'scriptUri', 'type': 'str'},
        'sha256_checksum': {'key': 'sha256Checksum', 'type': 'str'},
        'inline': {'key': 'inline', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(ImageTemplateShellCustomizer, self).__init__(**kwargs)
        self.script_uri = kwargs.get('script_uri', None)
        self.sha256_checksum = kwargs.get('sha256_checksum', None)
        self.inline = kwargs.get('inline', None)
        self.type = 'Shell'


class ImageTemplateUpdateParameters(Model):
    """Parameters for updating an image template.

    :param identity: The identity of the image template, if configured.
    :type identity: ~azure.mgmt.imagebuilder.models.ImageTemplateIdentity
    :param tags: The user-specified tags associated with the image template.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'identity': {'key': 'identity', 'type': 'ImageTemplateIdentity'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(ImageTemplateUpdateParameters, self).__init__(**kwargs)
        self.identity = kwargs.get('identity', None)
        self.tags = kwargs.get('tags', None)


class ImageTemplateVhdDistributor(ImageTemplateDistributor):
    """Distribute via VHD in a storage account.

    All required parameters must be populated in order to send to Azure.

    :param run_output_name: Required. The name to be used for the associated
     RunOutput.
    :type run_output_name: str
    :param artifact_tags: Tags that will be applied to the artifact once it
     has been created/updated by the distributor.
    :type artifact_tags: dict[str, str]
    :param type: Required. Constant filled by server.
    :type type: str
    """

    _validation = {
        'run_output_name': {'required': True, 'pattern': r'^[A-Za-z0-9-_.]{1,64}$'},
        'type': {'required': True},
    }

    _attribute_map = {
        'run_output_name': {'key': 'runOutputName', 'type': 'str'},
        'artifact_tags': {'key': 'artifactTags', 'type': '{str}'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ImageTemplateVhdDistributor, self).__init__(**kwargs)
        self.type = 'VHD'


class ImageTemplateVmProfile(Model):
    """Describes the virtual machine used to build, customize and capture images.

    :param vm_size: Size of the virtual machine used to build, customize and
     capture images. Omit or specify empty string to use the default
     (Standard_D1_v2).
    :type vm_size: str
    """

    _attribute_map = {
        'vm_size': {'key': 'vmSize', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ImageTemplateVmProfile, self).__init__(**kwargs)
        self.vm_size = kwargs.get('vm_size', None)


class InnerError(Model):
    """Inner error details.

    :param exception_type: The exception type.
    :type exception_type: str
    :param error_detail: The internal error message or exception dump.
    :type error_detail: str
    """

    _attribute_map = {
        'exception_type': {'key': 'exceptionType', 'type': 'str'},
        'error_detail': {'key': 'errorDetail', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(InnerError, self).__init__(**kwargs)
        self.exception_type = kwargs.get('exception_type', None)
        self.error_detail = kwargs.get('error_detail', None)


class Operation(Model):
    """A REST API operation.

    :param name: The operation name. This is of the format
     {provider}/{resource}/{operation}
    :type name: str
    :param display: The object that describes the operation.
    :type display: ~azure.mgmt.imagebuilder.models.OperationDisplay
    :param origin: The intended executor of the operation.
    :type origin: str
    :param properties: Properties of the operation.
    :type properties: object
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
        'origin': {'key': 'origin', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(Operation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display = kwargs.get('display', None)
        self.origin = kwargs.get('origin', None)
        self.properties = kwargs.get('properties', None)


class OperationDisplay(Model):
    """The object that describes the operation.

    :param provider: Friendly name of the resource provider.
    :type provider: str
    :param operation: The operation type. For example: read, write, delete, or
     listKeys/action
    :type operation: str
    :param resource: The resource type on which the operation is performed.
    :type resource: str
    :param description: The friendly name of the operation.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.operation = kwargs.get('operation', None)
        self.resource = kwargs.get('resource', None)
        self.description = kwargs.get('description', None)


class ProvisioningError(Model):
    """Describes the error happened when create or update an image template.

    :param provisioning_error_code: Error code of the provisioning failure.
     Possible values include: 'BadSourceType', 'BadPIRSource', 'BadISOSource',
     'BadManagedImageSource', 'BadSharedImageVersionSource',
     'BadCustomizerType', 'UnsupportedCustomizerType', 'NoCustomizerScript',
     'BadDistributeType', 'BadSharedImageDistribute', 'ServerError', 'Other'
    :type provisioning_error_code: str or
     ~azure.mgmt.imagebuilder.models.ProvisioningErrorCode
    :param message: Verbose error message about the provisioning failure
    :type message: str
    """

    _attribute_map = {
        'provisioning_error_code': {'key': 'provisioningErrorCode', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ProvisioningError, self).__init__(**kwargs)
        self.provisioning_error_code = kwargs.get('provisioning_error_code', None)
        self.message = kwargs.get('message', None)


class SubResource(Model):
    """The Sub Resource model definition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :param name: Required. Resource name
    :type name: str
    :ivar type: Resource type
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'required': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SubResource, self).__init__(**kwargs)
        self.id = None
        self.name = kwargs.get('name', None)
        self.type = None


class RunOutput(SubResource):
    """Represents an output that was created by running an image template.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :param name: Required. Resource name
    :type name: str
    :ivar type: Resource type
    :vartype type: str
    :param artifact_id: The resource id of the artifact.
    :type artifact_id: str
    :param artifact_uri: The location URI of the artifact.
    :type artifact_uri: str
    :ivar provisioning_state: Provisioning state of the resource. Possible
     values include: 'Creating', 'Updating', 'Succeeded', 'Failed', 'Deleting'
    :vartype provisioning_state: str or
     ~azure.mgmt.imagebuilder.models.ProvisioningState
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'required': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'artifact_id': {'key': 'properties.artifactId', 'type': 'str'},
        'artifact_uri': {'key': 'properties.artifactUri', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'ProvisioningState'},
    }

    def __init__(self, **kwargs):
        super(RunOutput, self).__init__(**kwargs)
        self.artifact_id = kwargs.get('artifact_id', None)
        self.artifact_uri = kwargs.get('artifact_uri', None)
        self.provisioning_state = None
