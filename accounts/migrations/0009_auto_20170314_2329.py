# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20170214_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldata',
            name='photo',
            field=models.FileField(null=True, upload_to=b'/home/mihail/PycharmProjects/MyBlog/media', blank=True),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='user',
            field=models.OneToOneField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
