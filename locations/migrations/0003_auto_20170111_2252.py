# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-11 22:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_location_lon_gra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='lon_gra',
            field=models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True),
        ),
    ]
