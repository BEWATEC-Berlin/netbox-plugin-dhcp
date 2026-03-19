from netbox.plugins import PluginTemplateExtension


class VirtualMachineDHCPPanel(PluginTemplateExtension):
    models = ['virtualization.virtualmachine']

    def right_page(self):
        vm = self.context['object']
        dhcp_configuration = getattr(vm, 'dhcp_configuration', None)
        return self.render(
            'netbox_plugin_dhcp/inc/vm_dhcp_panel.html',
            extra_context={'dhcp_configuration': dhcp_configuration},
        )


template_extensions = [VirtualMachineDHCPPanel]
