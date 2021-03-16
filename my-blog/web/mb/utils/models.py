from django.db import models


class TimestampMixin(models.Model):
    """
    Provides a mixin for annotating a DB object with created / updated timestamps
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
