# Generated initial migration for netbox_plugin_dhcp

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('virtualization', '0001_initial'),
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
                ('range_start', models.GenericIPAddressField(help_text='First IP address in the DHCP pool range.', protocol='IPv4', verbose_name='Range Start')),
                ('range_end', models.GenericIPAddressField(help_text='Last IP address in the DHCP pool range.', protocol='IPv4', verbose_name='Range End')),
                ('router', models.GenericIPAddressField(help_text='Default gateway/router option.', protocol='IPv4', verbose_name='Router')),
                ('dns_servers', models.CharField(default='1.1.1.1,8.8.8.8', help_text='Comma-separated DNS server IPv4 addresses.', max_length=512, verbose_name='DNS Servers')),
                ('connect_server', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='dhcp_configuration', to='virtualization.virtualmachine', verbose_name='ConnectServer')),
            ],
            options={
                'verbose_name': 'DHCP Configuration',
                'verbose_name_plural': 'DHCP Configurations',
                'ordering': ['connect_server'],
            },
        ),
    ]
