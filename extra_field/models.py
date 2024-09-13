from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType


class ExtraField(models.Model):
    """A Model to store extra fields for any model."""

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    parent_model = GenericForeignKey('content_type', 'object_id')

    key = models.SlugField(max_length=255)
    value = models.JSONField()

    class Meta:
        """Meta class for ExtraField model."""

        unique_together = ('content_type', 'object_id', 'key')

    def __str__(self):
        """String representation of ExtraField model."""
        return f"{self.key}: {self.value}"


class ExtraFieldModel(models.Model):
    """An abstract model to store extra fields for any model."""

    extra_fields = GenericRelation(ExtraField)

    def set_value(self, key, value):
        """Method to set extra field."""
        if value is None:
            return None

        obj, _ = ExtraField.objects.update_or_create(
            content_type=ContentType.objects.get_for_model(self),
            object_id=self.pk,
            key=key,
            defaults={'value': value}
        )
        return obj

    def get_value(self, key):
        """Method to get extra field."""
        try:
            return self.extra_fields.get(key=key).value
        except ExtraField.DoesNotExist:
            return None

    def get_keys(self):
        """Method to get all keys."""
        return self.extra_fields.values_list('key', flat=True)

    def delete_key(self, key):
        """Method to delete extra field."""
        self.extra_fields.filter(key=key).delete()
