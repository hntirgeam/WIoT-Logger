from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from home_logger_drf.home_logger import views

urlpatterns = [
    path('devices/', views.DeviceList.as_view()),
    path('devices/<int:pk>/', views.DeviceDetail.as_view()),
    path('me', views.UserDetail.as_view()),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path('api-auth/', include('rest_framework.urls')),
]
