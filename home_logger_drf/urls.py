from django.urls import include, path
from rest_framework.routers import DefaultRouter

from home_logger_drf.home_logger import views

router = DefaultRouter(trailing_slash=True)
router.register(r"users", views.UserViewSet)
router.register(r"devices", views.DeviceViewSet)
router.register(r"records", views.RecordViewSet)


urlpatterns = [
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
] + router.urls
