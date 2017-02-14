# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('massage', '0002_auto_20170118_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 18, 18, 27, 28, 846293, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
