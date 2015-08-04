# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0008_auto_20150802_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslot',
            name='is_full',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(max_length=100, choices=[(b'Pending', b'Pending'), (b'Accepted', b'Accepted'), (b'Standby', b'Standby')]),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='current_parts',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
