from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.utils import timezone
from shortuuid.django_fields import ShortUUIDField


class Device(models.Model):
    id = ShortUUIDField(length=16, max_length=40, prefix="id_", primary_key=True)
    api_key = ShortUUIDField(length=32, max_length=32)

    owner = models.ForeignKey(User, on_delete=CASCADE, related_name="devices")
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256, null=True, default=None)
    ip_address = models.GenericIPAddressField(null=True)
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-date_added"]

    def __repr__(self) -> str:
        return f"{self.owner} {self.owner} {self.name} {self.api_key}\n"


class Record(models.Model):
    id = ShortUUIDField(length=32, max_length=40, prefix="id_", primary_key=True)
    device = models.ForeignKey(Device, on_delete=DO_NOTHING, related_name="records")
    temp = models.DecimalField(max_digits=8, decimal_places=4, default=Decimal(0))
    humidity = models.DecimalField(max_digits=8, decimal_places=4, default=Decimal(0))
    pressure = models.DecimalField(max_digits=8, decimal_places=4, default=Decimal(0))
    co2 = models.DecimalField(max_digits=8, decimal_places=4, default=Decimal(0))
    etvoc = models.DecimalField(max_digits=8, decimal_places=4, default=Decimal(0))
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-timestamp"]

    def __repr__(self) -> str:
        return f"\nDevice {self.device.id}) {self.temp} {self.humidity} {self.pressure} {self.CO2} {self.eTVOC} {self.timestamp}\n"
