# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0004_auto_20150703_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researcher',
            name='dob',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]
