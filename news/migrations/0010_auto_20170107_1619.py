# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20170107_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='news_comments',
        ),
        migrations.AddField(
            model_name='comments',
            name='comments_news',
            field=models.ForeignKey(default=1, to='news.News'),
            preserve_default=False,
        ),
    ]
