# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0003_auto_20150627_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='researcher',
            field=models.ForeignKey(related_name=b'experiment', to='part_finder.Researcher'),
        ),
    ]
