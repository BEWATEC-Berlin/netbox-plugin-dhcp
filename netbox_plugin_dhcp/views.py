from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from netbox.views import generic
from virtualization.models import VirtualMachine

from . import forms, models, tables


class DHCPConfigurationListView(generic.ObjectListView):
    queryset = models.DHCPConfiguration.objects.all()
    table = tables.DHCPConfigurationTable
    filterset = None


class DHCPConfigurationView(generic.ObjectView):
    queryset = models.DHCPConfiguration.objects.all()


class DHCPConfigurationEditView(generic.ObjectEditView):
    queryset = models.DHCPConfiguration.objects.all()
    form = forms.DHCPConfigurationForm
    template_name = 'netbox_plugin_dhcp/dhcpconfiguration_edit.html'


class DHCPConfigurationDeleteView(generic.ObjectDeleteView):
    queryset = models.DHCPConfiguration.objects.all()


class DHCPConfigurationBulkDeleteView(generic.BulkDeleteView):
    queryset = models.DHCPConfiguration.objects.all()
    table = tables.DHCPConfigurationTable


def _get_vm_vrf_id(vm):
    if getattr(vm, 'primary_ip4', None) and getattr(vm.primary_ip4, 'vrf_id', None):
        return vm.primary_ip4.vrf_id

    primary_ip = getattr(vm, 'primary_ip', None)
    if primary_ip and getattr(primary_ip, 'vrf_id', None):
        return primary_ip.vrf_id

    for interface in vm.interfaces.all():
        for ip_address in interface.ip_addresses.all():
            if ip_address.vrf_id:
                return ip_address.vrf_id

    return None


def ajax_connect_server_vrf(request, vm_id):
    vm = get_object_or_404(VirtualMachine, pk=vm_id)
    vrf_id = _get_vm_vrf_id(vm)
    return JsonResponse({'vm_id': vm.id, 'vrf_id': vrf_id})
