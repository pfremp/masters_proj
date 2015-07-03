# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0007_auto_20150703_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='address',
            field=models.CharField(max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='currency',
            field=models.CharField(blank=True, max_length=100, choices=[(b'Credits', b'Credits'), (b'Money', b'Money')]),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='long_description',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='no_of_participants_wanted',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='pmt_type',
            field=models.CharField(blank=True, max_length=128, choices=[(b'Total', b'Total'), (b'Hourly', b'Hourly')]),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='short_description',
            field=models.CharField(max_length=128, blank=True),
        ),
    ]
