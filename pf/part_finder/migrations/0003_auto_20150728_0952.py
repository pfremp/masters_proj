# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0002_timeslot_current_parts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='Experiment',
            new_name='experiment',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='Participant',
            new_name='participant',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='Researcher',
            new_name='researcher',
        ),
        migrations.AddField(
            model_name='application',
            name='terms',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='application',
            name='timeslot',
            field=models.OneToOneField(related_name='application', null=True, to='part_finder.TimeSlot'),
        ),
    ]
