# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0003_auto_20150829_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='no_of_parts',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
