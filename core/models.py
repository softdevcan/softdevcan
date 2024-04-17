from django.db import models

class GeneralSettings(models.Model):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )
    description = models.TextField(
        default='',
        max_length=1000,
        blank=True,
    )
    parameter = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )
    updated_Date = models.DateTimeField(
        auto_now=True,
        blank=True,
    )
    created_Date = models.DateTimeField(
        auto_now_add=True,
        blank=True,
    )

    def __str__(self):
        return self.name