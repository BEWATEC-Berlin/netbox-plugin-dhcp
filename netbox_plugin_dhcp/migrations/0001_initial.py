# Generated initial migration for netbox_plugin_dhcp

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ipam', '__first__'),
        ('virtualization', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='DHCPConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict)),
                ('default_lease_time', models.PositiveIntegerField(default=3600, help_text='Default lease time in seconds.', verbose_name='Default Lease Time')),
                ('max_lease_time', models.PositiveIntegerField(default=7200, help_text='Maximum lease time in seconds.', verbose_name='Max Lease Time')),
                ('address_range', models.ForeignKey(help_text='DHCP pool range object used for allocations.', on_delete=django.db.models.deletion.PROTECT, related_name='dhcp_configurations', to='ipam.iprange', verbose_name='Address Range')),
                ('connect_server', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='dhcp_configuration', to='virtualization.virtualmachine', verbose_name='ConnectServer')),
                ('prefix', models.ForeignKey(help_text='Prefix that contains the selected DHCP range.', on_delete=django.db.models.deletion.PROTECT, related_name='dhcp_configurations', to='ipam.prefix', verbose_name='Prefix')),
                ('router', models.ForeignKey(blank=True, help_text='Optional default gateway/router option.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='dhcp_router_for', to='ipam.ipaddress', verbose_name='Router')),
            ],
            options={
                'verbose_name': 'DHCP Configuration',
                'verbose_name_plural': 'DHCP Configurations',
                'ordering': ['connect_server'],
            },
        ),
        migrations.AddField(
            model_name='dhcpconfiguration',
            name='dns_servers',
            field=models.ManyToManyField(blank=True, help_text='Optional DNS server IP objects.', related_name='dhcp_dns_for', to='ipam.ipaddress', verbose_name='DNS Servers'),
        ),
    ]
