# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('massage', '0003_message_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='asker',
        ),
        migrations.AddField(
            model_name='message',
            name='asker',
            field=models.ForeignKey(related_name='asker_mails', default=0, blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(related_name='sending_mails', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
