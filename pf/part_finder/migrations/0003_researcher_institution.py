# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0002_delete_counter'),
    ]

    operations = [
        migrations.AddField(
            model_name='researcher',
            name='institution',
            field=models.CharField(blank=True, max_length=128, null=True, choices=[(b'Glasgow', b'University of Glasgow'), (b'Strathclyde', b'Strathclyde University')]),
            preserve_default=True,
        ),
    ]
