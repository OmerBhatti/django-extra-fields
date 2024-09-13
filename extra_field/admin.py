from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from extra_field.models import ExtraField

class ExtraFieldModelInline(GenericTabularInline):
    """An inline model to display extra fields for any model."""

    model = ExtraField
    extra = 1

admin.site.register(ExtraField)
