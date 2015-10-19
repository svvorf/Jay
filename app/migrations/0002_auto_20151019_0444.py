# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='friends',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='outgoing_requests',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='hour_span',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)], default=4),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='hour_start',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(23), django.core.validators.MinValueValidator(0)], default=20),
        ),
    ]
