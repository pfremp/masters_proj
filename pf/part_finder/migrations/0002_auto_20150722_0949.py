# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experiment',
            name='date',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='no_of_participants_wanted',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='start_time',
        ),
    ]
