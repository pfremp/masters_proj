# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0004_auto_20150719_2020'),
        ('part_finder', '0015_remove_experiment_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='location',
            field=models.ForeignKey(to='cities_light.City', null=True),
        ),
    ]
