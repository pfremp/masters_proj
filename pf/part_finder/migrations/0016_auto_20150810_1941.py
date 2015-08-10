# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0015_auto_20150810_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='city_only',
            field=models.BooleanField(default=False),
        ),
    ]
