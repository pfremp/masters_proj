# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0003_locations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='short_description',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='researcher',
            name='institution',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
    ]
