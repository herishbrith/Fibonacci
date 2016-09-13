# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-13 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Compute', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('ipId', models.AutoField(primary_key=True, serialize=False)),
                ('ipAddress', models.CharField(max_length=40)),
                ('visits', models.IntegerField(default=1)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
