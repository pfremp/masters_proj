# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0013_remove_userprofile_participant'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='participant',
            field=models.OneToOneField(null=True, blank=True, to='part_finder.Participant'),
            preserve_default=True,
        ),
    ]
