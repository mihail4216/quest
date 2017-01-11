# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_auto_20170111_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comments_news',
            field=models.ForeignKey(blank=True, to='news.News', null=True),
        ),
    ]
