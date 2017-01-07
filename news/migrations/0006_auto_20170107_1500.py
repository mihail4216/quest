# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20170107_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='news_comment',
        ),
        migrations.AddField(
            model_name='comments',
            name='comments_news',
            field=models.ForeignKey(default=1, to='news.News'),
            preserve_default=False,
        ),
    ]
