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

    class Meta:
        model = DHCPConfiguration
        fields = [
            'id',
            'url',
            'display',
            'connect_server',
            'default_lease_time',
            'max_lease_time',
            'range_start',
            'range_end',
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
