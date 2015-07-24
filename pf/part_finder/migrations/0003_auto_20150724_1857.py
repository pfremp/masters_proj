# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0002_auto_20150724_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='city',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
