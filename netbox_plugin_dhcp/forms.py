import ipaddress

from django import forms
from netbox.forms import NetBoxModelForm
from utilities.forms.fields import DynamicModelChoiceField
from utilities.forms.rendering import FieldSet
from virtualization.models import VirtualMachine

from .models import DHCPConfiguration


class DHCPConfigurationForm(NetBoxModelForm):
    fieldsets = (
        FieldSet('connect_server', name='Assignment'),
        FieldSet('default_lease_time', 'max_lease_time', name='Lease'),
        FieldSet('range_start', 'range_end', name='Range'),
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

    class Meta:
        model = DHCPConfiguration
        fields = [
            'connect_server',
            'default_lease_time',
            'max_lease_time',
            'range_start',
            'range_end',
            'router',
            'dns_servers',
            'tags',
        ]

    def clean_dns_servers(self):
        raw_value = self.cleaned_data.get('dns_servers', '')
        values = [value.strip() for value in raw_value.split(',') if value.strip()]

        if not values:
            raise forms.ValidationError('At least one DNS server is required.')

        for value in values:
            try:
                ipaddress.IPv4Address(value)
            except ValueError as exc:
                raise forms.ValidationError(f'Invalid DNS server IP: {value}') from exc

        return ','.join(values)


class DHCPConfigurationFilterForm(forms.Form):
    connect_server = DynamicModelChoiceField(
        queryset=VirtualMachine.objects.all(),
        required=False,
        label='ConnectServer',
    )
