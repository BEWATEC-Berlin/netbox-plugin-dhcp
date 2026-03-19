from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from netaddr import IPAddress
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
    address_range = models.ForeignKey(
        to='ipam.IPRange',
        on_delete=models.PROTECT,
        related_name='dhcp_configurations',
        verbose_name='Address Range',
        help_text='DHCP pool range object used for allocations.',
    )
    prefix = models.ForeignKey(
        to='ipam.Prefix',
        on_delete=models.PROTECT,
        related_name='dhcp_configurations',
        verbose_name='Prefix',
        help_text='Prefix that contains the selected DHCP range.',
        null=True,
        blank=True,
    )
    router = models.ForeignKey(
        to='ipam.IPAddress',
        on_delete=models.PROTECT,
        related_name='dhcp_router_for',
        verbose_name='Router',
        help_text='Optional default gateway/router option.',
        null=True,
        blank=True,
    )
    dns_servers = models.ManyToManyField(
        to='ipam.IPAddress',
        related_name='dhcp_dns_for',
        verbose_name='DNS Servers',
        help_text='Optional DNS server IP objects.',
        blank=True,
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

        if self.router and self.router.address.version != 4:
            raise ValidationError({'router': 'Router must be an IPv4 address.'})

        if self.prefix and self.address_range:
            if self.prefix.vrf_id != self.address_range.vrf_id:
                raise ValidationError({'address_range': 'Address range VRF must match the selected prefix VRF.'})

            prefix_network = self.prefix.prefix
            if IPAddress(self.address_range.start_address) not in prefix_network or IPAddress(self.address_range.end_address) not in prefix_network:
                raise ValidationError({'address_range': 'Address range must be fully contained in the selected prefix.'})
