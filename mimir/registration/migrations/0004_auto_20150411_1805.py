# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20150411_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='description',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='interests',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
