from netbox.api.viewsets import NetBoxModelViewSet

from ..models import DHCPConfiguration
from .serializers import DHCPConfigurationSerializer


class DHCPConfigurationViewSet(NetBoxModelViewSet):
    queryset = DHCPConfiguration.objects.all()
    serializer_class = DHCPConfigurationSerializer
