# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0011_auto_20150722_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='location',
            field=models.ForeignKey(to='cities_light.City', null=True),
        ),
    ]
