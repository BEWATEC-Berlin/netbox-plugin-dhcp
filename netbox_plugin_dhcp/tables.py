import django_tables2 as tables
from netbox.tables import NetBoxTable, columns

from .models import DHCPConfiguration


class DHCPConfigurationTable(NetBoxTable):
    connect_server = tables.Column(linkify=True)
    range = tables.Column(accessor='range_start', verbose_name='Range', orderable=False)
    actions = columns.ActionsColumn()

    def render_range(self, record):
        return f'{record.range_start} - {record.range_end}'

    class Meta(NetBoxTable.Meta):
        model = DHCPConfiguration
        fields = (
            'pk',
            'id',
            'connect_server',
            'default_lease_time',
            'max_lease_time',
            'range',
            'router',
            'dns_servers',
            'created',
            'last_updated',
            'actions',
        )
        default_columns = (
            'id',
            'connect_server',
            'default_lease_time',
            'max_lease_time',
            'range',
            'router',
            'actions',
        )
