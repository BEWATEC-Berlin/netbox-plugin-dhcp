from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '__first__'),
        ('netbox_plugin_dhcp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dhcpconfiguration',
            name='prefix',
            field=models.ForeignKey(
                blank=True,
                null=True,
                help_text='Prefix that contains the selected DHCP range.',
                on_delete=django.db.models.deletion.PROTECT,
                related_name='dhcp_configurations',
                to='ipam.prefix',
                verbose_name='Prefix',
            ),
        ),
    ]
