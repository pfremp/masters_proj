# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0013_auto_20150722_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='location',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
