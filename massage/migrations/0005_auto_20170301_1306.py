# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('massage', '0004_auto_20170214_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='asker',
            field=models.ForeignKey(related_name='asker_mails', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
