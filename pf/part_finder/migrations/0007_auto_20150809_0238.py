# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0006_auto_20150809_0234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experiment',
            old_name='student_online',
            new_name='student_only',
        ),
    ]
