from axes.signals import user_locked_out
from django.dispatch import receiver
from rest_framework.exceptions import PermissionDenied

from home_logger_drf import settings


@receiver(user_locked_out)
def raise_permission_denied(*args, **kwargs):
    raise PermissionDenied(f"Too many failed login attempts. Try in {settings.AXES_COOLOFF_TIME} minute")
