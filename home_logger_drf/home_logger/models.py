from django.contrib.auth.models import User
from django.db import models
from decimal import Decimal
from django.utils import timezone


from django.db.models.deletion import CASCADE, DO_NOTHING

class Device(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, related_name="device")
    name = models.CharField(max_length=32, null=True, default=None)
    description = models.CharField(max_length=256, null=True, default=None)
    mac_address = models.CharField(max_length=20, null=True, default=None)
    ip_address = models.GenericIPAddressField()
    date_added = models.DateTimeField(default=timezone.now)

class Record(models.Model):
    device = models.ForeignKey(Device, on_delete=DO_NOTHING, related_name="record")
    temp = models.DecimalField(max_digits=8, decimal_places=4, default=Decimal(0))
    humidity = models.DecimalField(max_digits=8, decimal_places=4, default=Decimal(0))
    pressure = models.DecimalField(max_digits=8, decimal_places=4, default=Decimal(0))
    CO2 = models.DecimalField(max_digits=8, decimal_places=4, default=Decimal(0))
    eTVOC = models.DecimalField(max_digits=8, decimal_places=4, default=Decimal(0))
    timestamp = models.DateTimeField(default=timezone.now)
    