# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20170107_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_comments',
            field=models.OneToOneField(to='news.Comments'),
        ),
    ]
