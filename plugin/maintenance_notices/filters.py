from nautobot.utilities.filters import BaseFilterSet
from .models import MaintenanceNotice
import django_filters
from django.utils import timezone


class MaintenanceNoticeFilterSet(django_filters.FilterSet):
    active = django_filters.BooleanFilter(method='filter_active')
    class Meta:
        model = MaintenanceNotice
        fields = ('start_time', 'end_time', 'duration', 'devices', 'created_by')
    def filter_active(self, queryset, name, value):
        if value:
            return queryset.filter(end_time__gt=timezone.now())
        else:
            return queryset.exclude(end_time__gt=timezone.now())