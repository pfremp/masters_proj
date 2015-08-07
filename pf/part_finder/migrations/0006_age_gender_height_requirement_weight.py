# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0005_auto_20150807_1136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('min_age', models.IntegerField(default=1)),
                ('max_age', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.CharField(max_length=128, choices=[(b'male', b'male'), (b'female', b'female')])),
            ],
        ),
        migrations.CreateModel(
            name='Height',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('height', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('match', models.BooleanField(default=False)),
                ('student', models.CharField(default=b'NO', max_length=128, choices=[(b'NO', b'NO'), (b'YES', b'YES')])),
                ('age', models.CharField(default=b'NO', max_length=128, choices=[(b'NO', b'NO'), (b'YES', b'YES')])),
                ('language', models.CharField(default=b'NO', max_length=128, choices=[(b'NO', b'NO'), (b'YES', b'YES')])),
                ('height', models.CharField(default=b'NO', max_length=128, choices=[(b'NO', b'NO'), (b'YES', b'YES')])),
                ('weight', models.CharField(default=b'NO', max_length=128, choices=[(b'NO', b'NO'), (b'YES', b'YES')])),
                ('gender', models.CharField(default=b'NO', max_length=128, choices=[(b'NO', b'NO'), (b'YES', b'YES')])),
                ('experiment', models.ForeignKey(default=b'NO', to='part_finder.Experiment')),
            ],
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.IntegerField(default=0)),
            ],
        ),
    ]
