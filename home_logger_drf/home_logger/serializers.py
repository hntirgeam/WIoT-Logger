from django.core.exceptions import PermissionDenied, ValidationError
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from home_logger_drf.home_logger import models


class UserSerializer(serializers.ModelSerializer):
    devices_amount = SerializerMethodField()

    class Meta:
        model = models.User
        fields = ["id", "username", "devices_amount"]

    def get_devices_amount(self, obj):
        return models.Device.objects.filter(owner=obj).count()


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = models.Device
        fields = ["owner", "id", "name", "description", "ip_address", "api_key", "date_added"]
        extra_kwargs = {"ip_address": {"required": False},
                        "date_added": {"required": False}}

    def create(self, validated_data):
        user = self.context["request"].user
        device = models.Device.objects.create(owner=user, **validated_data)
        return device


class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Record
        fields = ["id", "temp", "humidity", "pressure", "co2", "etvoc", "timestamp"]

    def create(self, validated_data):
        api_key = self.context["request"].data.get("api_key", None)
        device = None

        if not api_key:
            raise PermissionDenied
        try:
            device = models.Device.objects.get(api_key=api_key)
        except (models.Device.DoesNotExist, ValidationError):
            raise PermissionDenied
        
        record = models.Record.objects.create(device=device, **validated_data)
        return record
