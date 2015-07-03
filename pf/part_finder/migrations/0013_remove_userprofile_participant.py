# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0012_auto_20150703_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='participant',
        ),
    ]
