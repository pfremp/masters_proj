# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0007_auto_20150821_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='revised',
            field=models.BooleanField(default=False),
        ),
    ]
