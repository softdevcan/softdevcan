# Generated by Django 4.2.11 on 2024-04-18 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_imagesetting_alter_generalsettings_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generalsettings',
            old_name='created_Date',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='generalsettings',
            old_name='updated_Date',
            new_name='updated_date',
        ),
        migrations.RenameField(
            model_name='imagesetting',
            old_name='created_Date',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='imagesetting',
            old_name='updated_Date',
            new_name='updated_date',
        ),
    ]