# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0010_payment_experiment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experiment',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='paid_event',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='payment_amount',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='pmt_type',
        ),
    ]
