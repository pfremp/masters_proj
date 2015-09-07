# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0002_auto_20150906_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
