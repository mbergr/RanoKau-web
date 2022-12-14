# Generated by Django 4.1.2 on 2022-11-10 21:58

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0014_alter_userprofile_friends'),
        ('projects', '0008_remove_project_company_remove_project_complete_per_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='company',
            field=models.ForeignKey(default='RanoKau', on_delete=django.db.models.deletion.CASCADE, to='register.company'),
        ),
        migrations.AddField(
            model_name='project',
            name='complete_per',
            field=models.FloatField(default=0, max_length=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('1', 'Stuck'), ('2', 'Working'), ('3', 'Done')], default=1, max_length=7),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('1', 'Stuck'), ('2', 'Working'), ('3', 'Done')], default=1, max_length=7),
        ),
    ]
