# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0009_auto_20150703_1001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='address_line_1',
            new_name='address_line_11',
        ),
    ]
