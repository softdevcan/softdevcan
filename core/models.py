from django.db import models

class AbstractModel(models.Model):
    updated_date = models.DateTimeField(
        auto_now=True,
        blank=True,
        verbose_name='Updated Date',
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        verbose_name='Created Date',
    )
    class Meta:
        abstract = True
class GeneralSettings(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='Name of the setting',
    )
    description = models.TextField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text='Description of the setting',
    )
    parameter = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Parameter',
        help_text='Parameter of the setting',
    )
    def __str__(self):
        return f"General Settings: {self.name}"

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ['name']

class ImageSetting(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of the setting.',
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text='',
    )
    file = models.ImageField(
        default='',
        verbose_name='Image',
        help_text='',
        blank=True,
        upload_to='images/',
    )

    def __str__(self):
        return f'Image Setting: {self.name}'

    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'
        ordering = ('name',)