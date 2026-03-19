from netbox.api.serializers import NetBoxModelSerializer
from rest_framework import serializers

from ..models import DHCPConfiguration


def _build_url(request, obj):
    if request is not None:
        return request.build_absolute_uri(obj.get_absolute_url())
    return obj.get_absolute_url()


class DHCPConfigurationSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_plugin_dhcp-api:dhcpconfiguration-detail'
    )
    connect_server = serializers.SerializerMethodField()
    prefix = serializers.SerializerMethodField()
    address_range = serializers.SerializerMethodField()
    router = serializers.SerializerMethodField()
    dns_servers = serializers.SerializerMethodField()

    class Meta:
        model = DHCPConfiguration
        fields = [
            'id',
            'url',
            'display',
            'connect_server',
            'default_lease_time',
            'max_lease_time',
            'prefix',
            'address_range',
            'router',
            'dns_servers',
            'created',
            'last_updated',
            'tags',
            'custom_fields',
        ]

    def get_connect_server(self, obj):
        if obj.connect_server:
            return {
                'id': obj.connect_server.id,
                'name': obj.connect_server.name,
                'url': _build_url(self.context.get('request'), obj.connect_server),
            }
        return None

    def get_prefix(self, obj):
        if obj.prefix:
            return {
                'id': obj.prefix.id,
                'display': str(obj.prefix),
                'url': _build_url(self.context.get('request'), obj.prefix),
            }
        return None

    def get_address_range(self, obj):
        if obj.address_range:
            return {
                'id': obj.address_range.id,
                'display': str(obj.address_range),
                'url': _build_url(self.context.get('request'), obj.address_range),
            }
        return None

    def get_router(self, obj):
        if obj.router:
            return {
                'id': obj.router.id,
                'display': str(obj.router),
                'url': _build_url(self.context.get('request'), obj.router),
            }
        return None

    def get_dns_servers(self, obj):
        return [
            {
                'id': dns.id,
                'display': str(dns),
                'url': _build_url(self.context.get('request'), dns),
            }
            for dns in obj.dns_servers.all()
        ]
