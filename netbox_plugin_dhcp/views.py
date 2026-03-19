from netbox.views import generic

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


class DHCPConfigurationDeleteView(generic.ObjectDeleteView):
    queryset = models.DHCPConfiguration.objects.all()


class DHCPConfigurationBulkDeleteView(generic.BulkDeleteView):
    queryset = models.DHCPConfiguration.objects.all()
    table = tables.DHCPConfigurationTable
