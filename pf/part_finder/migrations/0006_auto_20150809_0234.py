# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0005_auto_20150808_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='online',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='experiment',
            name='student_online',
            field=models.BooleanField(default=False),
        ),
    ]
