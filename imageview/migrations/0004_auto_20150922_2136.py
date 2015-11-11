# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imageview', '0003_auto_20150918_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=100, default=''),
        ),
    ]
