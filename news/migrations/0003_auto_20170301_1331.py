# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0002_auto_20170301_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='people',
        ),
        migrations.AddField(
            model_name='news',
            name='people',
            field=models.ManyToManyField(related_name='people', null=True, to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
