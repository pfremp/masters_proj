# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0016_auto_20150810_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='uni_only',
        ),
    ]
