from home_logger_drf.home_logger import models
from home_logger_drf.home_logger import serializers
from home_logger_drf.home_logger.permissions import IsOwner

from rest_framework import permissions
from rest_framework import generics


class UserList(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    
    
class DeviceList(generics.ListCreateAPIView):
    queryset = models.Device.objects.all()
    serializer_class = serializers.DeviceSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Device.objects.all()
    serializer_class = serializers.DeviceSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
