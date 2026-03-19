# NetBox DHCP Plugin

NetBox plugin for managing Kea DHCP configuration objects assigned to ConnectServer VMs.

## Goal

This plugin stores the DHCP values needed to render Kea configuration from a VM context.  
Each DHCP configuration is assigned to exactly one VM with role `connectserver`.

Configurable values include:
- default lease time
- max lease time
- DHCP range (start/end)
- router (gateway)
- DNS servers

## Features

- Native NetBox plugin model (`DHCPConfiguration`)
- One configuration per ConnectServer VM (`OneToOneField`)
- Validation that the assigned VM has role `connectserver`
- UI list/detail/add/edit/delete pages
- Plugin navigation entry
- VM right-side panel showing DHCP configuration
- API endpoint for automation

## Compatibility

- NetBox 4.5+
- Python 3.8+

## Installation

```bash
pip install .
```

Add to NetBox `configuration.py`:

```python
PLUGINS = ['netbox_plugin_dhcp']
```

Run migrations:

```bash
python manage.py migrate
```

Restart NetBox services.

## API

Base route:

`/api/plugins/dhcp/dhcp-configs/`

## Kea render usage (example)

In VM-related rendering logic, use the assigned object (if present):

```python
cfg = vm.dhcp_configuration

kea_subnet = {
	"pools": [{"pool": f"{cfg.range_start} - {cfg.range_end}"}],
	"option-data": [
		{"name": "routers", "data": cfg.router},
		{"name": "domain-name-servers", "data": cfg.dns_servers},
	],
	"valid-lifetime": cfg.default_lease_time,
	"max-valid-lifetime": cfg.max_lease_time,
}
```

