# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0003_auto_20150807_0957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='lang',
        ),
        migrations.AddField(
            model_name='participant',
            name='lang',
            field=models.ManyToManyField(related_name='participant', to='part_finder.Languages'),
        ),
    ]
