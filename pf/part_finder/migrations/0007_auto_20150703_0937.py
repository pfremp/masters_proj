# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0006_auto_20150703_0914'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experiment',
            old_name='payment_type',
            new_name='currency',
        ),
        migrations.AddField(
            model_name='experiment',
            name='pmt_type',
            field=models.CharField(default=1, max_length=128, choices=[(b'Total', b'Total'), (b'Hourly', b'Hourly')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='experiment',
            name='payment_amount',
            field=models.IntegerField(max_length=1000, blank=True),
        ),
    ]
