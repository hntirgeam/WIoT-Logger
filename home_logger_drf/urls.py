from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from home_logger_drf.home_logger import views

urlpatterns = [
    path('devices/', views.DeviceList.as_view()),
    path('devices/<int:pk>/', views.DeviceDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]