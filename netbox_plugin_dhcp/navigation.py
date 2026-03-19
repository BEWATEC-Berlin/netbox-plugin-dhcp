from netbox.plugins import PluginMenuButton, PluginMenuItem

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_plugin_dhcp:dhcpconfiguration_list',
        link_text='DHCP Configurations',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_plugin_dhcp:dhcpconfiguration_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
            ),
        ),
    ),
)
