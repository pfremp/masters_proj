# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cities_light', '0004_auto_20150719_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('terms', models.BooleanField(default=False)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=100)),
                ('sender', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('currency', models.CharField(max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dummy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.ForeignKey(to='cities_light.Country')),
                ('parent', models.ForeignKey(blank=True, to='part_finder.Dummy', null=True)),
                ('region', models.ForeignKey(to='cities_light.Region')),
            ],
        ),
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('short_description', models.CharField(max_length=128, blank=True)),
                ('long_description', models.CharField(max_length=500, blank=True)),
                ('duration', models.FloatField(blank=True)),
                ('address', models.CharField(max_length=128, blank=True)),
                ('language_req', models.CharField(max_length=128, blank=True)),
                ('url', models.URLField(blank=True)),
                ('researcher_slug', models.SlugField(null=True, blank=True)),
                ('slug', models.SlugField(unique=True, null=True, blank=True)),
                ('is_full', models.BooleanField(default=False)),
                ('has_ended', models.BooleanField(default=False)),
                ('city', models.ForeignKey(to='cities_light.City', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Is_paid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_paid', models.CharField(max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dob', models.DateField(default=datetime.date.today, null=True, verbose_name=b'Date')),
                ('contact_number', models.IntegerField(max_length=128, null=True, blank=True)),
                ('occupation', models.CharField(max_length=128, blank=True)),
                ('lang', models.CharField(max_length=128, blank=True)),
                ('education', models.CharField(blank=True, max_length=1000, choices=[(b'School', b'School'), (b'SQ1', b'School Qualification1'), (b'College', b'College'), (b'University', b'University')])),
                ('student', models.BooleanField(default=False)),
                ('course_name', models.CharField(max_length=100)),
                ('year', models.IntegerField(null=True)),
                ('matric', models.CharField(max_length=20, null=True)),
                ('gender', models.CharField(blank=True, max_length=128, choices=[(b'Male', b'Male'), (b'Female', b'Female'), (b'PNTS', b'Prefer not to say')])),
                ('height', models.IntegerField(max_length=128, null=True, blank=True)),
                ('weight', models.IntegerField(max_length=128, null=True, blank=True)),
                ('max_distance', models.IntegerField(max_length=128, null=True, blank=True)),
                ('uni_only', models.BooleanField(default=False)),
                ('online_only', models.BooleanField(default=False)),
                ('paid_only', models.BooleanField(default=False)),
                ('email_notifications', models.BooleanField(default=False)),
                ('city', models.ForeignKey(to='cities_light.City', null=True)),
                ('country', models.ForeignKey(to='cities_light.Country', null=True)),
                ('experiments', models.ManyToManyField(related_name='participants', null=True, to='part_finder.Experiment', blank=True)),
                ('region', models.ForeignKey(to='cities_light.Region', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField(null=True)),
                ('currency', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'is_paid', chained_field=b'is_paid', auto_choose=True, to='part_finder.Currency')),
                ('experiment', models.ForeignKey(related_name='experiment', to='part_finder.Experiment', null=True)),
                ('is_paid', models.ForeignKey(to='part_finder.Is_paid')),
            ],
        ),
        migrations.CreateModel(
            name='Payment_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('payment_type', models.CharField(max_length=128, null=True)),
                ('currency', models.ForeignKey(to='part_finder.Currency')),
            ],
        ),
        migrations.CreateModel(
            name='Researcher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('department', models.CharField(max_length=128, null=True, blank=True)),
                ('contact_no', models.IntegerField()),
                ('url', models.URLField(max_length=128, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=datetime.date.today, null=True, verbose_name=b'Date')),
                ('start_time', models.TimeField(null=True, blank=True)),
                ('end_time', models.TimeField(null=True, blank=True)),
                ('no_of_parts', models.IntegerField(null=True, blank=True)),
                ('current_parts', models.IntegerField(null=True, blank=True)),
                ('is_full', models.BooleanField(default=False)),
                ('experiment', models.ForeignKey(related_name='timeslot', to='part_finder.Experiment', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('typex', models.CharField(max_length=128, verbose_name=b'type')),
                ('participant', models.OneToOneField(related_name='userprofile', null=True, blank=True, to='part_finder.Participant')),
                ('researcher', models.OneToOneField(related_name='userprofile', null=True, blank=True, to='part_finder.Researcher')),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='researcher',
            name='university',
            field=models.ForeignKey(blank=True, to='part_finder.University', null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_type',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'currency', to='part_finder.Payment_type', chained_field=b'currency'),
        ),
        migrations.AddField(
            model_name='participant',
            name='university',
            field=models.ForeignKey(blank=True, to='part_finder.University', null=True),
        ),
        migrations.AddField(
            model_name='experiment',
            name='researcher',
            field=models.ForeignKey(related_name='experiment', to='part_finder.Researcher'),
        ),
        migrations.AddField(
            model_name='currency',
            name='is_paid',
            field=models.ForeignKey(to='part_finder.Is_paid', null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='experiment',
            field=models.ForeignKey(related_name='application', to='part_finder.Experiment', null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='participant',
            field=models.ForeignKey(related_name='application', to='part_finder.Participant', null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='researcher',
            field=models.ForeignKey(related_name='application', to='part_finder.Researcher', null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='timeslot',
            field=models.ForeignKey(related_name='application', to='part_finder.TimeSlot', null=True),
        ),
    ]
