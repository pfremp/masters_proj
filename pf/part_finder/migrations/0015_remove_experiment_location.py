# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0014_auto_20150722_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experiment',
            name='location',
        ),
    ]
