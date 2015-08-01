# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0006_remove_application_terms'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='terms',
            field=models.BooleanField(default=False),
        ),
    ]
