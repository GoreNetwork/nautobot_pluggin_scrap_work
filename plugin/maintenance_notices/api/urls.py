from nautobot.core.api.routers import OrderedDefaultRouter
from maintenance_notices.api import views

router = OrderedDefaultRouter()
router.register("", views.MaintenanceNoticeViewSet)
urlpatterns = router.urls