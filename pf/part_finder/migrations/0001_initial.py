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
                ('name', models.CharField(max_length=128, blank=True)),
                ('expId', models.CharField(default=5, max_length=128, unique=True, serialize=False, primary_key=True)),
                ('date', models.DateField(default=datetime.date.today, verbose_name=b'Date', blank=True)),
                ('paidEvent', models.CharField(max_length=128, choices=[(b'Y', b'Yes'), (b'N', b'No')])),
                ('location', models.CharField(max_length=128)),
                ('noOfPartsWanted', models.IntegerField(default=0)),
                ('endTime', models.TimeField(null=True, blank=True)),
                ('startTime', models.TimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'Participant Name', max_length=128)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('dob', models.DateField(default=datetime.date.today, verbose_name=b'Date', blank=True)),
                ('matric', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('contactNo', models.IntegerField(max_length=128, blank=True)),
                ('address', models.CharField(max_length=128)),
                ('occupation', models.CharField(max_length=128, blank=True)),
                ('maritial', models.CharField(max_length=128, blank=True)),
                ('gender', models.CharField(max_length=128, blank=True)),
                ('ethnicity', models.CharField(max_length=128, blank=True)),
                ('religion', models.CharField(max_length=128, blank=True)),
                ('height', models.IntegerField(max_length=128, null=True, blank=True)),
                ('weight', models.IntegerField(max_length=128, null=True, blank=True)),
                ('max_distance', models.IntegerField(max_length=128, null=True, blank=True)),
                ('online_only', models.IntegerField(max_length=128, null=True, blank=True)),
                ('paid_only', models.CharField(blank=True, max_length=128, choices=[(b'Y', b'Yes'), (b'N', b'No')])),
                ('email_notifications', models.CharField(blank=True, max_length=128, choices=[(b'Y', b'Yes'), (b'N', b'No')])),
                ('experiment', models.ManyToManyField(to='part_finder.Experiment', null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Researcher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'Researcher Name', max_length=128)),
                ('matric', models.CharField(max_length=128)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
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
