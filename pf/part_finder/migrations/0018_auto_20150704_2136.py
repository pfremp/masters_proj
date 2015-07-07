# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0017_auto_20150704_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='idz',
        ),
        migrations.AddField(
            model_name='participant',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
