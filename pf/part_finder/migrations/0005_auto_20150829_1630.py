# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0004_auto_20150829_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='current_parts',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
