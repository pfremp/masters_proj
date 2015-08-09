# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0008_auto_20150809_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gender',
            name='gender',
            field=models.CharField(max_length=128, choices=[(b'male', b'Male'), (b'female', b'Female')]),
        ),
        migrations.AlterField(
            model_name='matchingdetail',
            name='gender',
            field=models.CharField(blank=True, max_length=128, choices=[(b'male', b'Male'), (b'female', b'Female')]),
        ),
    ]
