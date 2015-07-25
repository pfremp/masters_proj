# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslot',
            name='current_parts',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
