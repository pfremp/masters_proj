# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchingDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.CharField(blank=True, max_length=128, choices=[(b'male', b'male'), (b'female', b'female')])),
                ('min_age', models.IntegerField(default=1, blank=True)),
                ('max_age', models.IntegerField(default=1, blank=True)),
                ('height', models.IntegerField(default=0, blank=True)),
                ('weight', models.IntegerField(default=0, blank=True)),
                ('language', models.CharField(max_length=128, blank=True)),
                ('requirement', models.ForeignKey(related_name='matchdetails', to='part_finder.Requirement', null=True)),
            ],
        ),
    ]
