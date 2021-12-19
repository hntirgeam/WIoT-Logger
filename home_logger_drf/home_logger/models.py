import uuid
from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.utils import timezone


class Device(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE, related_name="devices")
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256, null=True, default=None)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    ip_address = models.GenericIPAddressField(null=True)
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-date_added"]

    def __repr__(self) -> str:
        return f"{self.owner} {self.owner} {self.name} {self.uuid}\n"


class Record(models.Model):
    device = models.ForeignKey(Device, on_delete=DO_NOTHING, related_name="records")
    temp = models.DecimalField(max_digits=8, decimal_places=4, default=Decimal(0))
    humidity = models.DecimalField(max_digits=8, decimal_places=4, default=Decimal(0))
    pressure = models.DecimalField(max_digits=8, decimal_places=4, default=Decimal(0))
    CO2 = models.DecimalField(max_digits=8, decimal_places=4, default=Decimal(0))
    eTVOC = models.DecimalField(max_digits=8, decimal_places=4, default=Decimal(0))
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-timestamp"]

    def __repr__(self) -> str:
        return f"\nDevice {self.device.id}) {self.temp} {self.humidity} {self.pressure} {self.CO2} {self.eTVOC} {self.timestamp}\n"
