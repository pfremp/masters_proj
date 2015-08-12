# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0004_auto_20150812_1825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experiment',
            name='short_description',
        ),
    ]
