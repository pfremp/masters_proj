# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0011_auto_20150809_1842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experiment',
            name='lang',
        ),
    ]
