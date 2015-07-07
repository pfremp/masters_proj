# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0018_auto_20150704_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='researcher',
            field=models.OneToOneField(related_name=b'userprofile', null=True, blank=True, to='part_finder.Researcher'),
        ),
    ]
