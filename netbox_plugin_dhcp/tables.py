import django_tables2 as tables
from netbox.tables import NetBoxTable, columns

from .models import DHCPConfiguration


class DHCPConfigurationTable(NetBoxTable):
    connect_server = tables.Column(linkify=True)
    address_range = tables.Column(linkify=True, verbose_name='Range')
    actions = columns.ActionsColumn()

    class Meta(NetBoxTable.Meta):
        model = DHCPConfiguration
        fields = (
            'pk',
            'id',
            'connect_server',
            'default_lease_time',
            'max_lease_time',
            'address_range',
            'router',
            'created',
            'last_updated',
            'actions',
        )
        default_columns = (
            'id',
            'connect_server',
            'default_lease_time',
            'max_lease_time',
            'address_range',
            'router',
            'actions',
        )
