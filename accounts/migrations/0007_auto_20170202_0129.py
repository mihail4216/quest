# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20170202_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldata',
            name='photo',
            field=models.FileField(null=True, upload_to=b'/home/mihail/PycharmProjects/MyBlog/static/image', blank=True),
        ),
    ]
