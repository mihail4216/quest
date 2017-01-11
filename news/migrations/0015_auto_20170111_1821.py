# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_auto_20170111_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='avtor',
            field=models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comments_news',
            field=models.OneToOneField(null=True, blank=True, to='news.News'),
        ),
        migrations.AlterField(
            model_name='news',
            name='avtor',
            field=models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
