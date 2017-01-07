# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20170105_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comments_news',
        ),
        migrations.AddField(
            model_name='news',
            name='news_comment',
            field=models.ForeignKey(default=1, to='news.Comments'),
            preserve_default=False,
        ),
    ]
