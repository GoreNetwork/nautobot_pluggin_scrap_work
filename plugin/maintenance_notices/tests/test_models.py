from nautobot.utilities.testing import TestCase

from maintenance_notices import models
from datetime import datetime, timedelta, timezone

class TestMaintenanceNotice(TestCase):
    """Test Maintenance Notice Model."""
    @classmethod
    def setUpTestData(cls):
        cls.maintenance = models.MaintenanceNotice.objects.create(
            start_time=datetime.now(timezone.utc),
            duration=30,
        )
    def test_end_time(self):
        # import pdb; pdb.set_trace()
        self.assertEqual(
            self.maintenance.end_time, 
            self.maintenance.start_time + timedelta(minutes=self.maintenance.duration),
        )