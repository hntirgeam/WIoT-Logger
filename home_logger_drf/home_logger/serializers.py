from rest_framework import serializers

from home_logger_drf.home_logger import models



class UserSerializer(serializers.ModelSerializer):
    devices = serializers.PrimaryKeyRelatedField(many=True, queryset=models.Device.objects.all())

    class Meta:
        model = models.User
        fields = ['id', 'username', 'devices']

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = models.Device
        fields = ['owner', 'name', 'description', 'mac_address', 'ip_address']
        extra_kwargs = {"user": {"required": False}}
