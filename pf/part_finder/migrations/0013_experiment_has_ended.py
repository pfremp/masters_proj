# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0012_auto_20150805_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='has_ended',
            field=models.BooleanField(default=False),
        ),
    ]
