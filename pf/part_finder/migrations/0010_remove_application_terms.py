# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0009_remove_experiment_revised'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='terms',
        ),
    ]