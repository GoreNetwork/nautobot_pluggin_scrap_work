from django.contrib import admin
from maintenance_notices.models import MaintenanceNotice

@admin.register(MaintenanceNotice)
class MaintenanceNoticeAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'created_by')