# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0006_experiment_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='language',
            field=models.ManyToManyField(default=None, related_name='participant', to='part_finder.Languages', blank=True),
        ),
    ]
