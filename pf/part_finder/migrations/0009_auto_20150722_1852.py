# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('part_finder', '0008_remove_location_street'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('currency', models.CharField(max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField(null=True)),
                ('currency', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'is_paid', chained_field=b'is_paid', auto_choose=True, to='part_finder.Currency')),
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
        migrations.RenameModel(
            old_name='Continent',
            new_name='Is_paid',
        ),
        migrations.RemoveField(
            model_name='area',
            name='country',
        ),
        migrations.RemoveField(
            model_name='country',
            name='continent',
        ),
        migrations.RemoveField(
            model_name='location',
            name='area',
        ),
        migrations.RemoveField(
            model_name='location',
            name='continent',
        ),
        migrations.RemoveField(
            model_name='location',
            name='country',
        ),
        migrations.RenameField(
            model_name='is_paid',
            old_name='continent',
            new_name='is_paid',
        ),
        migrations.DeleteModel(
            name='Area',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.AddField(
            model_name='payment',
            name='is_paid',
            field=models.ForeignKey(to='part_finder.Is_paid'),
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_type',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'currency', to='part_finder.Payment_type', chained_field=b'currency'),
        ),
        migrations.AddField(
            model_name='currency',
            name='is_paid',
            field=models.ForeignKey(to='part_finder.Is_paid'),
        ),
    ]
