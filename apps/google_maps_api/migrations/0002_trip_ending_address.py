# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-15 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google_maps_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='ending_address',
            field=models.CharField(max_length=38, null=True),
        ),
    ]
