from django.dispatch import receiver

from axes.signals import user_locked_out
from rest_framework.exceptions import PermissionDenied
from home_logger_drf import settings

@receiver(user_locked_out)
def raise_permission_denied(*args, **kwargs):
    raise PermissionDenied(F"Too many failed login attempts. Try in {settings.AXES_COOLOFF_TIME} minute")