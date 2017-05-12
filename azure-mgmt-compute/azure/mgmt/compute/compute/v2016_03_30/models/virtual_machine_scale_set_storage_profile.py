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


class VirtualMachineScaleSetStorageProfile(Model):
    """Describes a virtual machine scale set storage profile.

    :param image_reference: The image reference.
    :type image_reference: :class:`ImageReference
     <azure.mgmt.compute.compute.v2016_03_30.models.ImageReference>`
    :param os_disk: The OS disk.
    :type os_disk: :class:`VirtualMachineScaleSetOSDisk
     <azure.mgmt.compute.compute.v2016_03_30.models.VirtualMachineScaleSetOSDisk>`
    """

    _attribute_map = {
        'image_reference': {'key': 'imageReference', 'type': 'ImageReference'},
        'os_disk': {'key': 'osDisk', 'type': 'VirtualMachineScaleSetOSDisk'},
    }

    def __init__(self, image_reference=None, os_disk=None):
        self.image_reference = image_reference
        self.os_disk = os_disk
