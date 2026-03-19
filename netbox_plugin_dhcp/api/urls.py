from netbox.api.routers import NetBoxRouter

from .views import DHCPConfigurationViewSet

app_name = 'netbox_plugin_dhcp'

router = NetBoxRouter()
router.register('dhcp-configs', DHCPConfigurationViewSet)

urlpatterns = router.urls
