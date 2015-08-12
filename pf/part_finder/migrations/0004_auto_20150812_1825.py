# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0003_participant_reg_2_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='contact_number',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='height',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='weight',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
