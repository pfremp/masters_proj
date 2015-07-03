# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0011_auto_20150703_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='graduation_year',
            field=models.IntegerField(),
        ),
    ]
