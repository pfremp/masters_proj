# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0003_auto_20150808_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matchingdetail',
            old_name='language',
            new_name='l',
        ),
    ]
