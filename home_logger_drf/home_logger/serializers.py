from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from django.core.exceptions import PermissionDenied, ValidationError
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
        fields = ["owner", "id", "name", "description", "ip_address", "uuid"]
        extra_kwargs = {"ip_address": {"required": False}}

    def create(self, validated_data):
        user = self.context["request"].user
        device = models.Device.objects.create(owner=user, **validated_data)
        return device


class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Record
        fields = ["id", "temp", "humidity", "pressure", "CO2", "eTVOC", "timestamp"]

    def create(self, validated_data):
        uuid = self.context["request"].data.get("uuid", None)
        device = None

        if not uuid:
            raise PermissionDenied
        try:
            device = models.Device.objects.get(uuid=uuid)
        except (models.Device.DoesNotExist, ValidationError):
            raise PermissionDenied

        record = models.Record.objects.create(device=device, **validated_data)
        return record
