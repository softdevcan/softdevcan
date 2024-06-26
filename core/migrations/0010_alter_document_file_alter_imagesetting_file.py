# Generated by Django 4.2.11 on 2024-04-19 13:17

from django.db import migrations, models
import resume.custom_storage


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_rename_generalsettings_generalsetting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(blank=True, default='', storage=resume.custom_storage.DocumentStorage(), upload_to='', verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='imagesetting',
            name='file',
            field=models.ImageField(blank=True, default='', upload_to=resume.custom_storage.ImageSettingStorage(), verbose_name='Image'),
        ),
    ]
