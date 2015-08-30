# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0002_auto_20150829_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='current_parts',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
