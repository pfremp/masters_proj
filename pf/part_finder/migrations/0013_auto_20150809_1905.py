# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0012_remove_experiment_lang'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchingdetail',
            name='l',
            field=models.CharField(max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='matchingdetail',
            name='language',
            field=models.ManyToManyField(related_name='matchingdetail', to='part_finder.Languages'),
        ),
    ]
