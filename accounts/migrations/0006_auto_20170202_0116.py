# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_personaldata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldata',
            name='city',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='hbd',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='phone',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='photo',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
