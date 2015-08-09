# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0010_participant_lang'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matchingdetail',
            name='l',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='lang',
        ),
        migrations.AddField(
            model_name='matchingdetail',
            name='language',
            field=models.ManyToManyField(related_name='matchingdetail', to='part_finder.Languages', blank=True),
        ),
    ]
