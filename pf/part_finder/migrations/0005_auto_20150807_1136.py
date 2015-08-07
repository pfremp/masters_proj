# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0004_auto_20150807_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='lang',
            field=models.ManyToManyField(related_name='participant', null=True, to='part_finder.Languages'),
        ),
    ]
