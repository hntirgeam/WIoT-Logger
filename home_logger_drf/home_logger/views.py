from home_logger_drf.home_logger import models
from home_logger_drf.home_logger import serializers
from home_logger_drf.home_logger.permissions import IsOwner

from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.request import Request 
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response    

class UserViewSet(GenericViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
    permission_classes=[permissions.IsAuthenticated]
    
    @action(detail=False, methods=["get"], url_path="me", permission_classes=[permissions.IsAuthenticated])
    def me(self, request: Request):
        user = request.user
        devices = user.devices.all()
        serializer = serializers.UserSerializer(user)
        d_serializer = serializers.DeviceSerializer(devices, many=True)

        response = {
            **serializer.data,
            "devices": d_serializer.data
        }
        return Response(response)


class DeviceViewSet(viewsets.ModelViewSet, GenericViewSet):
    serializer_class = serializers.DeviceSerializer
    queryset = models.Device.objects.all()
    permission_classes=[permissions.IsAuthenticated, IsOwner]
    
    def list(self, request, *args, **kwargs):
        devices = models.Device.objects.filter(owner=request.user)
        serializer = serializers.DeviceSerializer(devices, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, *args, **kwargs):
        device = self.get_object()
        records = device.records.all()
        serializer = serializers.DeviceSerializer(device)
        r_serializer = serializers.RecordSerializer(records, many=True)
        
        response = {
            **serializer.data,
            "records": r_serializer.data,
        }
        return Response(response)
    
    # @action TODO: action for exporting csv data

        
class RecordViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = serializers.RecordSerializer
    queryset = models.Record.objects.all()
    