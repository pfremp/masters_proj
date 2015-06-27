# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('date', models.DateField(default=datetime.date.today, verbose_name=b'Date')),
                ('paidEvent', models.BooleanField(default=False)),
                ('location', models.CharField(max_length=128, choices=[(b'Gla', b'Glasgow'), (b'Ldn', b'London')])),
                ('noOfPartsWanted', models.IntegerField(null=True)),
                ('endTime', models.TimeField(blank=True)),
                ('startTime', models.TimeField(blank=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=128)),
                ('occupation', models.CharField(max_length=128, blank=True)),
                ('marital', models.CharField(max_length=128, blank=True)),
                ('gender', models.CharField(max_length=128, blank=True)),
                ('ethnicity', models.CharField(max_length=128, blank=True)),
                ('religion', models.CharField(max_length=128, blank=True)),
                ('height', models.IntegerField(max_length=128, null=True, blank=True)),
                ('weight', models.IntegerField(max_length=128, null=True, blank=True)),
                ('max_distance', models.IntegerField(max_length=128, null=True, blank=True)),
                ('online_only', models.IntegerField(max_length=128, null=True, blank=True)),
                ('paid_only', models.CharField(blank=True, max_length=128, choices=[(b'Y', b'Yes'), (b'N', b'No')])),
                ('email_notifications', models.CharField(blank=True, max_length=128, choices=[(b'Y', b'Yes'), (b'N', b'No')])),
                ('experiments', models.ManyToManyField(related_name=b'participants', null=True, to='part_finder.Experiment', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Researcher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dob', models.DateField(default=datetime.date.today)),
                ('matric', models.IntegerField()),
                ('institution', models.CharField(max_length=128, choices=[(b'Glasgow', b'University of Glasgow'), (b'Strathclyde', b'Strathclyde University')])),
                ('contactNo', models.IntegerField()),
                ('department', models.CharField(max_length=128, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('typex', models.CharField(max_length=128, verbose_name=b'type')),
                ('participant', models.OneToOneField(null=True, blank=True, to='part_finder.Participant')),
                ('researcher', models.OneToOneField(null=True, blank=True, to='part_finder.Researcher')),
                ('user', models.OneToOneField(related_name=b'profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='experiment',
            name='researcher',
            field=models.ForeignKey(to='part_finder.Researcher'),
            preserve_default=True,
        ),
    ]
