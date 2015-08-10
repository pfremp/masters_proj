# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0014_remove_matchingdetail_language'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='max_distance',
            new_name='city_only',
        ),
        migrations.RenameField(
            model_name='participant',
            old_name='email_notifications',
            new_name='eligible_only',
        ),
        migrations.AddField(
            model_name='participant',
            name='my_uni_only',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='application',
            name='terms',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='requirement',
            name='experiment',
            field=models.ForeignKey(related_name='requirement', to='part_finder.Experiment'),
        ),
    ]
