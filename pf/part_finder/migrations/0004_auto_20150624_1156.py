# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0003_researcher_institution'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='maritial',
            new_name='marital',
        ),
    ]
