"""Django urlpatterns declaration for maintenance_notices app."""
from django.urls import path

from maintenance_notices import views

urlpatterns = [
    # MaintenanceNotice URLs
    path("maintenancenotice/", views.MaintenanceNoticeListView.as_view(), name="maintenancenotice_list"),
    path("maintenancenotice/add/", views.MaintenanceNoticeCreateView.as_view(), name="maintenancenotice_add"),
    path("maintenancenotice/<uuid:pk>/", views.MaintenanceNoticeView.as_view(), name="maintenancenotice"),
    path("maintenancenotice/<uuid:pk>/delete/", views.MaintenanceNoticeDeleteView.as_view(), name="maintenancenotice_delete"),
    path("maintenancenotice/<uuid:pk>/edit/", views.MaintenanceNoticeEditView.as_view(), name="maintenancenotice_edit"),
    path('maintenancenotice/active/', views.ActiveMaintenanceNoticeListView.as_view(), name='maintenancenotice_active_list'),

]