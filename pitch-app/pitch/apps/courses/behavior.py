from django.db import models


class Timestampable(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True, null=True)

    class Meta:
        abstract = True
