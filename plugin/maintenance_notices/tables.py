"""Tables for nautobot_plugin_reservation."""
import django_tables2 as tables
from nautobot.utilities.tables import BaseTable, ButtonsColumn, ToggleColumn
from maintenance_notices import models


class MaintenanceNoticeTable(BaseTable):
    """Table for list view."""

    pk = ToggleColumn()
    start_time = tables.Column(linkify=True)
    actions = ButtonsColumn(
        models.MaintenanceNotice, buttons=("edit", "delete"), pk_field="pk"
    )

    class Meta(BaseTable.Meta):
        """Meta attributes."""

        model = models.MaintenanceNotice
        fields = ("pk", "start_time", "end_time", "duration", "comments", "created_by", "devices")