# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0010_auto_20150703_1259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='address_line_11',
            new_name='address_line_1',
        ),
    ]
