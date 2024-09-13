from django.db import models

from extra_field.models import ExtraFieldModel


class Blog(ExtraFieldModel):
    """A Model to store extra fields for any model."""
    title = models.CharField(max_length=255)
    content = models.TextField()

    objects = models.Manager()

    def __str__(self):
        """String representation of Blog model."""
        return self.title
