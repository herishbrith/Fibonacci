# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-13 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Compute', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('ipId', models.AutoField(primary_key=True, serialize=False)),
                ('ipAddress', models.CharField(max_length=40)),
                ('visits', models.IntegerField(default=0)),
            ],
        ),
    ]
