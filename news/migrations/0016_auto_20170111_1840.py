# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_auto_20170111_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='avtor',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comments_news',
            field=models.ForeignKey(blank=True, to='news.News', null=True),
        ),
    ]
