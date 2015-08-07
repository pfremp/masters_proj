# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0002_experiment_is_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lang', models.CharField(max_length=128)),
            ],
        ),
        migrations.AlterField(
            model_name='experiment',
            name='long_description',
            field=models.CharField(max_length=1000, blank=True),
        ),
    ]
