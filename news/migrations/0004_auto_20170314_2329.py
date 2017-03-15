# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20170301_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='people',
            field=models.ManyToManyField(related_name='people', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
