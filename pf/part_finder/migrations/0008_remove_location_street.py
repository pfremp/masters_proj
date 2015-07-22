# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0007_auto_20150722_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='street',
        ),
    ]
