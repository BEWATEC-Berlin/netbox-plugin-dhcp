from django import forms
from netbox.forms import NetBoxModelForm
from ipam.models import IPAddress, IPRange
from utilities.forms.fields import DynamicModelChoiceField, DynamicModelMultipleChoiceField
from utilities.forms.rendering import FieldSet
from virtualization.models import VirtualMachine

from .models import DHCPConfiguration


class DHCPConfigurationForm(NetBoxModelForm):
    fieldsets = (
        FieldSet('connect_server', name='Assignment'),
        FieldSet('default_lease_time', 'max_lease_time', name='Lease'),
        FieldSet('address_range', name='Range'),
        FieldSet('router', 'dns_servers', name='Network Options'),
        FieldSet('tags', name='Tags'),
    )

    connect_server = DynamicModelChoiceField(
        queryset=VirtualMachine.objects.all(),
        label='ConnectServer',
        query_params={
            'role': 'connectserver',
        },
    )
    connect_server_vrf = forms.IntegerField(required=False, widget=forms.HiddenInput)
    address_range = DynamicModelChoiceField(
        queryset=IPRange.objects.all(),
        label='Address Range',
        query_params={
            'family': 4,
            'vrf_id': '$connect_server_vrf',
        },
    )
    router = DynamicModelChoiceField(
        queryset=IPAddress.objects.all(),
        required=False,
        label='Router',
        query_params={
            'family': 4,
            'vrf_id': '$connect_server_vrf',
        },
    )
    dns_servers = DynamicModelMultipleChoiceField(
        queryset=IPAddress.objects.all(),
        required=False,
        label='DNS Servers',
        query_params={
            'family': 4,
            'vrf_id': '$connect_server_vrf',
        },
    )

    @staticmethod
    def _vm_vrf_id(vm):
        if not vm:
            return None

        if getattr(vm, 'primary_ip4', None) and getattr(vm.primary_ip4, 'vrf_id', None):
            return vm.primary_ip4.vrf_id

        primary_ip = getattr(vm, 'primary_ip', None)
        if primary_ip and getattr(primary_ip, 'vrf_id', None):
            return primary_ip.vrf_id

        return None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        vm = self.instance.connect_server if self.instance and self.instance.pk else None
        self.initial['connect_server_vrf'] = self._vm_vrf_id(vm)

    class Meta:
        model = DHCPConfiguration
        fields = [
            'connect_server',
            'default_lease_time',
            'max_lease_time',
            'address_range',
            'router',
            'dns_servers',
            'tags',
        ]

    def clean(self):
        super().clean()

        connect_server = self.cleaned_data.get('connect_server')
        vm_vrf_id = self._vm_vrf_id(connect_server)
        address_range = self.cleaned_data.get('address_range')
        router = self.cleaned_data.get('router')
        dns_servers = self.cleaned_data.get('dns_servers')

        if vm_vrf_id and address_range and address_range.vrf_id and address_range.vrf_id != vm_vrf_id:
            self.add_error('address_range', 'Address range VRF must match the ConnectServer VRF.')

        if router and router.address.version != 4:
            self.add_error('router', 'Router must be an IPv4 address.')
        if vm_vrf_id and router and router.vrf_id and router.vrf_id != vm_vrf_id:
            self.add_error('router', 'Router VRF must match the ConnectServer VRF.')

        for dns in dns_servers or []:
            if dns.address.version != 4:
                self.add_error('dns_servers', f'DNS server {dns} is not an IPv4 address.')
            if vm_vrf_id and dns.vrf_id and dns.vrf_id != vm_vrf_id:
                self.add_error('dns_servers', f'DNS server {dns} is not in the ConnectServer VRF.')

        return self.cleaned_data


class DHCPConfigurationFilterForm(forms.Form):
    connect_server = DynamicModelChoiceField(
        queryset=VirtualMachine.objects.all(),
        required=False,
        label='ConnectServer',
    )
