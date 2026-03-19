import ipaddress

from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel


class DHCPConfiguration(NetBoxModel):
    connect_server = models.OneToOneField(
        to='virtualization.VirtualMachine',
        on_delete=models.PROTECT,
        related_name='dhcp_configuration',
        verbose_name='ConnectServer',
    )
    default_lease_time = models.PositiveIntegerField(
        default=3600,
        verbose_name='Default Lease Time',
        help_text='Default lease time in seconds.',
    )
    max_lease_time = models.PositiveIntegerField(
        default=7200,
        verbose_name='Max Lease Time',
        help_text='Maximum lease time in seconds.',
    )
    range_start = models.GenericIPAddressField(
        protocol='IPv4',
        verbose_name='Range Start',
        help_text='First IP address in the DHCP pool range.',
    )
    range_end = models.GenericIPAddressField(
        protocol='IPv4',
        verbose_name='Range End',
        help_text='Last IP address in the DHCP pool range.',
    )
    router = models.GenericIPAddressField(
        protocol='IPv4',
        verbose_name='Router',
        help_text='Default gateway/router option.',
    )
    dns_servers = models.CharField(
        max_length=512,
        default='1.1.1.1,8.8.8.8',
        verbose_name='DNS Servers',
        help_text='Comma-separated DNS server IPv4 addresses.',
    )

    class Meta:
        verbose_name = 'DHCP Configuration'
        verbose_name_plural = 'DHCP Configurations'
        ordering = ['connect_server']

    def __str__(self):
        return f'DHCP - {self.connect_server}'

    def get_absolute_url(self):
        return reverse('plugins:netbox_plugin_dhcp:dhcpconfiguration', args=[self.pk])

    def clean(self):
        super().clean()

        if self.connect_server:
            role_slug = self.connect_server.role.slug if self.connect_server.role else None
            if role_slug != 'connectserver':
                raise ValidationError({'connect_server': 'ConnectServer VM role must be connectserver.'})

        if self.default_lease_time and self.max_lease_time:
            if self.default_lease_time > self.max_lease_time:
                raise ValidationError({'default_lease_time': 'Default lease time must be less than or equal to max lease time.'})

        if self.range_start and self.range_end:
            start_ip = ipaddress.IPv4Address(self.range_start)
            end_ip = ipaddress.IPv4Address(self.range_end)
            if start_ip > end_ip:
                raise ValidationError({'range_start': 'Range start must be less than or equal to range end.'})
