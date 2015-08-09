# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0009_auto_20150809_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='lang',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
