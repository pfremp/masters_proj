# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0009_auto_20150803_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='is_full',
            field=models.BooleanField(),
        ),
    ]
