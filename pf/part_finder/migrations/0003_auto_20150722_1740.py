# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0002_auto_20150722_0949'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('continent', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('continent', models.ForeignKey(to='part_finder.Continent')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=100)),
                ('area', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'country', to='part_finder.Area', chained_field=b'country')),
                ('continent', models.ForeignKey(to='part_finder.Continent')),
                ('country', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'continent', chained_field=b'continent', auto_choose=True, to='part_finder.Country')),
            ],
        ),
        migrations.AddField(
            model_name='area',
            name='country',
            field=models.ForeignKey(to='part_finder.Country'),
        ),
    ]
