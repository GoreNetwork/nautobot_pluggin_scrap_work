"""Forms for maintenance_notices."""
from django import forms
from nautobot.utilities.forms import (
    BootstrapMixin,
    DateTimePicker,
)

from maintenance_notices import models

class MaintenanceNoticeForm(BootstrapMixin, forms.ModelForm):
    """MaintenanceNotice creation/edit form."""
    
    #This adds a date picker when you click on the datetime feild
    start_time = forms.DateTimeField(
        widget=DateTimePicker(attrs={"placeholder": "Maintenance Start Date and Time"}),
        label="Start Time",
    )

    class Meta:
        """Meta attributes."""

        model = models.MaintenanceNotice
        fields = ("__all__")