# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0004_auto_20150728_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='experiment',
            field=models.ForeignKey(related_name='timeslot', to='part_finder.Experiment', null=True),
        ),
    ]
