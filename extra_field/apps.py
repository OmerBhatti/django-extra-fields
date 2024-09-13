from django.apps import AppConfig


class ExtraFieldConfig(AppConfig):
    """App config for extra_field."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'extra_field'
