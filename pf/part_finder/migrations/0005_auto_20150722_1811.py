# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0004_auto_20150722_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='area',
            field=models.ForeignKey(to='cities_light.City', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='country',
            field=models.ForeignKey(to='cities_light.Country', null=True),
        ),
    ]
