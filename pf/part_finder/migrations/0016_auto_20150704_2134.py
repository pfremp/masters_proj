# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0015_auto_20150703_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
