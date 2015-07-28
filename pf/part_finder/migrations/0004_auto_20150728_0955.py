# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0003_auto_20150728_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='experiment',
            field=models.ForeignKey(related_name='application', to='part_finder.Experiment', null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='participant',
            field=models.ForeignKey(related_name='application', to='part_finder.Participant', null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='researcher',
            field=models.ForeignKey(related_name='application', to='part_finder.Researcher', null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='timeslot',
            field=models.ForeignKey(related_name='application', to='part_finder.TimeSlot', null=True),
        ),
    ]
