# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Borehole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('borehole_ID', models.IntegerField()),
                ('name', models.CharField(default=b'None', max_length=30)),
                ('current_status', models.CharField(default=b'None', max_length=30)),
                ('contact_number', models.CharField(default=b'None', max_length=30)),
                ('lat', models.FloatField(null=True, verbose_name='Latitude', blank=True)),
                ('lon', models.FloatField(null=True, verbose_name='Longitude', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dict',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('borehole_id', models.IntegerField()),
                ('status', models.CharField(max_length=30)),
                ('datetime', models.DateTimeField()),
                ('description', models.CharField(default=b'N/A', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='StatusCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=40, db_index=True)),
                ('code', models.IntegerField(db_index=True)),
                ('container', models.ForeignKey(to='borehole.Dict')),
            ],
        ),
    ]
