from netbox.plugins import PluginConfig
from .version import __version__


class NetBoxDHCPConfig(PluginConfig):
    name = 'netbox_plugin_dhcp'
    verbose_name = 'DHCP Configuration'
    description = 'NetBox plugin for managing Kea DHCP configuration per ConnectServer VM'
    version = __version__
    author = 'ConnectedCare GmbH'
    author_email = ''
    base_url = 'dhcp'
    required_settings = []
    default_settings = {}
    min_version = '4.5.0'


config = NetBoxDHCPConfig

__all__ = ['__version__', 'config']
