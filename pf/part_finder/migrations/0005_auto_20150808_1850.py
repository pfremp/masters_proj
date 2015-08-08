# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0004_auto_20150808_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchingdetail',
            name='height',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='matchingdetail',
            name='max_age',
            field=models.IntegerField(default=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='matchingdetail',
            name='min_age',
            field=models.IntegerField(default=1, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='matchingdetail',
            name='weight',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
