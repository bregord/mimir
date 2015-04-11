# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_userprofile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discussions',
            name='author',
        ),
        migrations.RemoveField(
            model_name='discussions',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='discussions',
            name='seminar',
        ),
        migrations.RemoveField(
            model_name='seminar',
            name='author',
        ),
        migrations.DeleteModel(
            name='Discussions',
        ),
        migrations.DeleteModel(
            name='Seminar',
        ),
    ]
