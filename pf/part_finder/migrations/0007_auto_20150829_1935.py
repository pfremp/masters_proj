# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import part_finder.models


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0006_auto_20150829_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='no_of_parts',
            field=models.PositiveIntegerField(validators=[part_finder.models.validate_gt1]),
        ),
    ]
