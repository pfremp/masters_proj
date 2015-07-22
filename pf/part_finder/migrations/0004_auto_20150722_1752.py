# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0003_auto_20150722_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='area',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='country',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='continent',
            name='continent',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
