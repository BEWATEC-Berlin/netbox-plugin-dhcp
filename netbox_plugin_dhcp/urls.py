from django.urls import path
from netbox.views import generic

from . import models, views

urlpatterns = [
    path('ajax/connect-server-vrf/<int:vm_id>/', views.ajax_connect_server_vrf, name='ajax_connect_server_vrf'),
    path('dhcp-configs/', views.DHCPConfigurationListView.as_view(), name='dhcpconfiguration_list'),
    path('dhcp-configs/add/', views.DHCPConfigurationEditView.as_view(), name='dhcpconfiguration_add'),
    path('dhcp-configs/<int:pk>/', views.DHCPConfigurationView.as_view(), name='dhcpconfiguration'),
    path('dhcp-configs/<int:pk>/edit/', views.DHCPConfigurationEditView.as_view(), name='dhcpconfiguration_edit'),
    path('dhcp-configs/<int:pk>/delete/', views.DHCPConfigurationDeleteView.as_view(), name='dhcpconfiguration_delete'),
    path('dhcp-configs/<int:pk>/changelog/', generic.ObjectChangeLogView.as_view(), {'model': models.DHCPConfiguration}, name='dhcpconfiguration_changelog'),
    path('dhcp-configs/delete/', views.DHCPConfigurationBulkDeleteView.as_view(), name='dhcpconfiguration_bulk_delete'),
]
