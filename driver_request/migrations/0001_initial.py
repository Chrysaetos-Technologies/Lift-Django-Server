# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-10 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver_Request',
            fields=[
                ('request_id', models.IntegerField(primary_key=True, serialize=False)),
                ('source_lat', models.CharField(max_length=200)),
                ('source_long', models.CharField(max_length=200)),
                ('destination_lat', models.CharField(max_length=200)),
                ('destination_long', models.CharField(max_length=200)),
                ('timestamp', models.CharField(max_length=200)),
            ],
        ),
    ]
