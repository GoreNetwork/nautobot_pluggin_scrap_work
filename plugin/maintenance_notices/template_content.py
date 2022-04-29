from nautobot.extras.plugins import PluginTemplateExtension
from django.utils import timezone


class DeviceMaintenanceNotices(PluginTemplateExtension):
    """Display Maintenance Notices in a panel on device page."""

    model = 'dcim.device'

    def right_page(self):
        """Panel to display maintenance notices."""
        obj = self.context["object"]
        active_notices = obj.maintenance_notices.filter(end_time__gt=timezone.now())
        extra_context = {"active_notices": active_notices}
        return self.render(
            'maintenance_notices/device_notices.html',
            extra_context=extra_context,
        )


template_extensions = [DeviceMaintenanceNotices]