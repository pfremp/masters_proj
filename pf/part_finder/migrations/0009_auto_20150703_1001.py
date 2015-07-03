# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0008_auto_20150703_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='pmt_type',
            field=models.CharField(blank=True, max_length=128, choices=[(b'Total', b'Total'), (b'Hourly', b'Hourly'), (b'N/A', b'N/A')]),
        ),
    ]
