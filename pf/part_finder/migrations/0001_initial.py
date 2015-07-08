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
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=100, choices=[(b'Pending', b'Pending'), (b'Accepted', b'Accepted'), (b'Standby', b'Standby')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=100)),
                ('sender', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('short_description', models.CharField(max_length=128, blank=True)),
                ('long_description', models.CharField(max_length=500, blank=True)),
                ('date', models.DateField(default=datetime.date.today, verbose_name=b'Date')),
                ('start_time', models.TimeField(blank=True)),
                ('end_time', models.TimeField(blank=True)),
                ('duration', models.FloatField(blank=True)),
                ('paid_event', models.BooleanField(default=False)),
                ('currency', models.CharField(blank=True, max_length=100, choices=[(b'Credits', b'Credits'), (b'Money', b'Money')])),
                ('payment_amount', models.FloatField(max_length=1000, blank=True)),
                ('pmt_type', models.CharField(blank=True, max_length=128, choices=[(b'Total', b'Total'), (b'Hourly', b'Hourly'), (b'N/A', b'N/A')])),
                ('location', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=128, blank=True)),
                ('no_of_participants_wanted', models.IntegerField(null=True, blank=True)),
                ('slug', models.SlugField(unique=True, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address_line_1', models.CharField(max_length=128, blank=True)),
                ('address_line_2', models.CharField(max_length=128, blank=True)),
                ('city', models.CharField(max_length=128, blank=True)),
                ('postcode', models.CharField(max_length=128, blank=True)),
                ('contact_number', models.IntegerField(max_length=128, null=True, blank=True)),
                ('occupation', models.CharField(max_length=128, blank=True)),
                ('student', models.BooleanField(default=False)),
                ('course_name', models.CharField(max_length=100)),
                ('year', models.IntegerField(null=True)),
                ('matric', models.CharField(max_length=20, null=True)),
                ('gender', models.CharField(blank=True, max_length=128, choices=[(b'Male', b'Male'), (b'Female', b'Female')])),
                ('ethnicity', models.CharField(max_length=128, blank=True)),
                ('religion', models.CharField(max_length=128, blank=True)),
                ('height', models.IntegerField(max_length=128, null=True, blank=True)),
                ('weight', models.IntegerField(max_length=128, null=True, blank=True)),
                ('max_distance', models.IntegerField(max_length=128, null=True, blank=True)),
                ('uni_only', models.BooleanField(default=False)),
                ('online_only', models.BooleanField(default=False)),
                ('paid_only', models.BooleanField(default=False)),
                ('email_notifications', models.BooleanField(default=False)),
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
                ('dob', models.DateField(default=datetime.date.today, null=True, verbose_name=b'Date')),
                ('institution', models.CharField(max_length=128, null=True, blank=True)),
                ('contact_no', models.IntegerField()),
                ('department', models.CharField(max_length=128, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
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
                ('participant', models.OneToOneField(related_name=b'userprofile', null=True, blank=True, to='part_finder.Participant')),
                ('researcher', models.OneToOneField(related_name=b'userprofile', null=True, blank=True, to='part_finder.Researcher')),
                ('user', models.OneToOneField(related_name=b'profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='participant',
            name='university',
            field=models.ForeignKey(blank=True, to='part_finder.University', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='experiment',
            name='researcher',
            field=models.ForeignKey(related_name=b'experiment', to='part_finder.Researcher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='Experiment',
            field=models.OneToOneField(related_name=b'application', null=True, to='part_finder.Experiment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='Participant',
            field=models.OneToOneField(related_name=b'application', null=True, to='part_finder.Participant'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='Researcher',
            field=models.OneToOneField(related_name=b'application', null=True, to='part_finder.Researcher'),
            preserve_default=True,
        ),
    ]
