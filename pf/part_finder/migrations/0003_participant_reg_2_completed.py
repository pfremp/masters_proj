# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0002_auto_20150812_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='reg_2_completed',
            field=models.BooleanField(default=False),
        ),
    ]
