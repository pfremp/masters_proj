# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='country',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='region',
        ),
        migrations.AlterField(
            model_name='participant',
            name='city',
            field=models.ForeignKey(blank=True, to='cities_light.City', null=True),
        ),
    ]
