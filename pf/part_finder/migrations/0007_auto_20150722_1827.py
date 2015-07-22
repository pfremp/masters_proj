# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0006_auto_20150722_1812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='city',
        ),
        migrations.AddField(
            model_name='location',
            name='amount',
            field=models.IntegerField(null=True),
        ),
    ]
