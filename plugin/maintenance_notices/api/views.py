from nautobot.core.api.views import ModelViewSet
from maintenance_notices.models import MaintenanceNotice
from .serializers import MaintenanceNoticeSerializer
from maintenance_notices.filters import MaintenanceNoticeFilterSet


class MaintenanceNoticeViewSet(ModelViewSet):
    queryset = MaintenanceNotice.objects.all()
    filterset_class = MaintenanceNoticeFilterSet
    serializer_class = MaintenanceNoticeSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)