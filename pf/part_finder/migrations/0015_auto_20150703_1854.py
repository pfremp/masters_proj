# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0014_userprofile_participant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='graduation_year',
        ),
        migrations.AddField(
            model_name='participant',
            name='year',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='experiment',
            name='duration',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='payment_amount',
            field=models.FloatField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='contact_number',
            field=models.IntegerField(max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='participant',
            field=models.OneToOneField(related_name=b'userprofile', null=True, blank=True, to='part_finder.Participant'),
        ),
    ]
