# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publications',
            field=models.ManyToManyField(to=b'part_finder.Publication', blank=True),
        ),
    ]
