"""Maintenance Jobs."""
from nautobot.extras.jobs import Job, IntegerVar, MultiObjectVar
from nautobot.dcim.models import Device
from .models import MaintenanceNotice


name = "Maintenance Event Jobs"

class CheckDeviceMaintenanceEvents(Job):
    """Job that validates if a given date has an associated maintenance event."""
    devices = MultiObjectVar(model=Device)
    year = IntegerVar()
    month = IntegerVar()
    day = IntegerVar()

    class Meta:
        """Meta class for CheckDeviceMaintenanceEvents"""

        name = "Check Device Maintenance Events"
        description = "Verify if a maintenance event is associated to a device for a given date."
        read_only = True

    def run(self, data=None, commit=None):
        """Executes the job"""
        devices = data["devices"]
        year = data["year"]
        month = data["month"]
        day = data["day"]

        result = []
        for maintenance in MaintenanceNotice.objects.filter(
            start_time__year=year,
            start_time__month=month,
            start_time__day=day,
        ):
            for device in devices:
                if not maintenance.devices.filter(name=device.name).exists():
                    continue
                result.append(device)
                self.log_warning(
                    obj=device,
                    message=f"Impacted for {maintenance.duration} Minutes",
                )
        if not result:
            self.log_success(message=f"No devices impacted on this date.")
            return
        self.log_success(message=f"Job complete. A total of {len(result)} devices are impacted on this date.")        

jobs = [CheckDeviceMaintenanceEvents]        