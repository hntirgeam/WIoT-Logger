from home_logger_drf.home_logger import models
from home_logger_drf.home_logger import serializers
from home_logger_drf.home_logger.permissions import IsOwner

from rest_framework import permissions
from rest_framework import generics
from rest_framework.response import Response


class UserDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = serializers.UserSerializer(user)
        print(serializer.data)
        return Response(serializer.data)

    
    
class DeviceList(generics.ListCreateAPIView):
    queryset = models.Device.objects.all()
    serializer_class = serializers.DeviceSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
    def get(self, request, *args, **kwargs):
        user = request.user
        devices = user.devices.all()
        return Response(self.get_serializer(devices, many=True).data)

class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Device.objects.all()
    serializer_class = serializers.DeviceSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
