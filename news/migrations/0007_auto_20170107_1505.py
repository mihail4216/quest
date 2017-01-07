# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20170107_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comments_news',
        ),
        migrations.AddField(
            model_name='comments',
            name='title',
            field=models.CharField(default=2, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='news_comments',
            field=models.ForeignKey(default=1, to='news.Comments'),
            preserve_default=False,
        ),
    ]
