from nautobot.core.api.serializers import ValidatedModelSerializer
from maintenance_notices.models import MaintenanceNotice
from rest_framework.serializers import StringRelatedField


class MaintenanceNoticeSerializer(ValidatedModelSerializer):
    created_by = StringRelatedField(read_only=True)
    class Meta:
        model = MaintenanceNotice
        fields = ('id', 'start_time','end_time', 'duration', 'devices', 'created_by')