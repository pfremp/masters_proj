# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='education',
            field=models.CharField(blank=True, max_length=1000, choices=[(b'School', b'School'), (b'SQ1', b'School Qualification1'), (b'College', b'College'), (b'University', b'University')]),
        ),
    ]
