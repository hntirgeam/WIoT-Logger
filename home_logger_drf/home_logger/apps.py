from django.apps import AppConfig


class HomeLoggerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "home_logger_drf.home_logger"
    
    def ready(self):
        from home_logger_drf.home_logger import signals  # noqa
