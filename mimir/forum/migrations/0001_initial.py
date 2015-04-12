# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Discussions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contents', models.TextField()),
                ('line', models.IntegerField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(related_name='discussion_parent', blank=True, to='forum.Discussions')),
            ],
        ),
        migrations.CreateModel(
            name='Seminar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=50)),
                ('contents', models.TextField()),
                ('description', models.CharField(max_length=500)),
                ('date', models.DateTimeField(verbose_name=b'date written')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='discussions',
            name='seminar',
            field=models.ForeignKey(related_name='seminar', to='forum.Seminar'),
        ),
    ]
