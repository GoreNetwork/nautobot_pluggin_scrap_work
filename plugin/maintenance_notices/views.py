"""Views for maintenance_notices."""

from nautobot.core.views import generic
from django.conf import settings
from django.utils import timezone

from maintenance_notices import forms, models, tables

SETTINGS = settings.PLUGINS_CONFIG['maintenance_notices']
 

class MaintenanceNoticeListView(generic.ObjectListView):
    """List view."""

    queryset = models.MaintenanceNotice.objects.all()
    table = tables.MaintenanceNoticeTable
    action_buttons = ("add",)

class ActiveMaintenanceNoticeListView(MaintenanceNoticeListView):
    """List view for Active Notices."""

    queryset = models.MaintenanceNotice.objects.filter(end_time__gt=timezone.now())    

class MaintenanceNoticeView(generic.ObjectView):
    """Detail view."""

    queryset = models.MaintenanceNotice.objects.all()


class MaintenanceNoticeEditView(generic.ObjectEditView):
    """Edit view."""

    model = models.MaintenanceNotice
    queryset = models.MaintenanceNotice.objects.all()
    model_form = forms.MaintenanceNoticeForm

class MaintenanceNoticeCreateView(MaintenanceNoticeEditView):
    """Create view."""

    def alter_obj(self, obj, request, *args, **kwargs):
        """Insert user into object."""
        obj.created_by = request.user
        obj.duration = SETTINGS.get('default_duration')
        return obj
class MaintenanceNoticeDeleteView(generic.ObjectDeleteView):
    """Delete view."""

    model = models.MaintenanceNotice
    queryset = models.MaintenanceNotice.objects.all()    