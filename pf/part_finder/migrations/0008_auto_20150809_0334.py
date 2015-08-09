# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0007_auto_20150809_0238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matchingdetail',
            old_name='height',
            new_name='max_height',
        ),
        migrations.RenameField(
            model_name='matchingdetail',
            old_name='weight',
            new_name='max_weight',
        ),
        migrations.AddField(
            model_name='matchingdetail',
            name='min_height',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='matchingdetail',
            name='min_weight',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
