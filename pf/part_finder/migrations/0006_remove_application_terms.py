# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0005_auto_20150731_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='terms',
        ),
    ]
