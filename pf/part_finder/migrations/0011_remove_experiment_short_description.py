# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0010_remove_application_terms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experiment',
            name='short_description',
        ),
    ]
