# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0016_auto_20150704_2134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='id',
            new_name='idz',
        ),
    ]
