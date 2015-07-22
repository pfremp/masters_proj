# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0009_auto_20150722_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='experiment',
            field=models.ForeignKey(related_name='experiment', to='part_finder.Experiment', null=True),
        ),
    ]
