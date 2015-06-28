# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0002_auto_20150627_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='type',
            new_name='typex',
        ),
    ]
