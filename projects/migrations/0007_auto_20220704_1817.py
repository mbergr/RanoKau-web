# Generated by Django 2.2 on 2022-07-04 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='project',
            name='lon',
        ),
    ]
