# Generated by Django 3.2.9 on 2021-11-27 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='save_location',
            new_name='location',
        ),
    ]
