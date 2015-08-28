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
                ('status', models.CharField(max_length=100)),
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
            name='Experiment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('long_description', models.CharField(max_length=1000, null=True, blank=True)),
                ('duration', models.FloatField(null=True, blank=True)),
                ('address', models.CharField(max_length=128, blank=True)),
                ('url', models.URLField(blank=True)),
                ('researcher_slug', models.SlugField(null=True, blank=True)),
                ('slug', models.SlugField(unique=True, null=True, blank=True)),
                ('is_full', models.BooleanField(default=False)),
                ('has_ended', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('online', models.BooleanField(default=False)),
                ('student_only', models.BooleanField(default=False)),
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
            name='Languages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='MatchingDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.CharField(blank=True, max_length=128, choices=[(b'male', b'Male'), (b'female', b'Female')])),
                ('min_age', models.IntegerField(default=1, null=True, blank=True)),
                ('max_age', models.IntegerField(default=100, null=True, blank=True)),
                ('min_height', models.IntegerField(default=0, null=True, blank=True)),
                ('max_height', models.IntegerField(default=0, null=True, blank=True)),
                ('min_weight', models.IntegerField(default=0, null=True, blank=True)),
                ('max_weight', models.IntegerField(default=0, null=True, blank=True)),
                ('l', models.CharField(max_length=128, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dob', models.DateField(default=datetime.date.today, null=True, verbose_name=b'Date')),
                ('contact_number', models.IntegerField(null=True, blank=True)),
                ('occupation', models.CharField(max_length=128, blank=True)),
                ('education', models.CharField(blank=True, max_length=1000, choices=[(b'HS', b'High School Level'), (b'SCQF3', b'  -Access 3 / Foundation Standard Grade'), (b'SCQF4', b'-Intermediate 1 / General Standard Grade'), (b'SCQF5', b'-Intermediate 2 / Credit Standard Grade'), (b'GCSE', b'-GCSE'), (b'SCQF6', b'-Higher'), (b'ALEVEL', b'-A Level'), (b'SCQF7', b'-Advanced Higher'), (b'College', b'College Level'), (b'HNC', b'-HNC'), (b'HND', b'-HND'), (b'HE', b'University Level'), (b'HE1', b'-Bachelors  Degree'), (b'HE2', b'-Honours  Degree'), (b'HE3', b'-Masters  Degree'), (b'HE4', b'-Doctorates')])),
                ('student', models.BooleanField(default=False)),
                ('course_name', models.CharField(max_length=100)),
                ('year', models.IntegerField(null=True)),
                ('matric', models.CharField(max_length=20, null=True)),
                ('gender', models.CharField(blank=True, max_length=128, choices=[(b'Male', b'Male'), (b'Female', b'Female'), (b'PNTS', b'Prefer not to say')])),
                ('height', models.IntegerField(null=True, blank=True)),
                ('weight', models.IntegerField(null=True, blank=True)),
                ('city_only', models.BooleanField(default=False)),
                ('my_uni_only', models.BooleanField(default=False)),
                ('online_only', models.BooleanField(default=False)),
                ('paid_only', models.BooleanField(default=False)),
                ('eligible_only', models.BooleanField(default=False)),
                ('reg_2_completed', models.BooleanField(default=False)),
                ('city', models.ForeignKey(blank=True, to='cities_light.City', null=True)),
                ('experiments', models.ManyToManyField(related_name='participants', to='part_finder.Experiment', blank=True)),
                ('language', models.ManyToManyField(default=None, related_name='participant', to='part_finder.Languages', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.FloatField(null=True)),
                ('currency', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'is_paid', chained_field=b'is_paid', auto_choose=True, to='part_finder.Currency')),
                ('experiment', models.ForeignKey(related_name='payment', to='part_finder.Experiment', null=True)),
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
            name='Requirement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('match', models.BooleanField(default=False)),
                ('student', models.CharField(max_length=128, choices=[(b'0', b'NO'), (b'1', b'YES')])),
                ('age', models.CharField(max_length=128, choices=[(b'0', b'NO'), (b'1', b'YES')])),
                ('language', models.CharField(max_length=128, choices=[(b'0', b'NO'), (b'1', b'YES')])),
                ('height', models.CharField(max_length=128, choices=[(b'0', b'NO'), (b'1', b'YES')])),
                ('weight', models.CharField(max_length=128, choices=[(b'0', b'NO'), (b'1', b'YES')])),
                ('gender', models.CharField(max_length=128, choices=[(b'0', b'NO'), (b'1', b'YES')])),
                ('experiment', models.ForeignKey(related_name='requirement', to='part_finder.Experiment')),
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
            model_name='matchingdetail',
            name='requirement',
            field=models.ForeignKey(related_name='matchdetail', to='part_finder.Requirement', null=True),
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
