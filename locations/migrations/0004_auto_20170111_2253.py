# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-11 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_auto_20170111_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='elev',
            field=models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='lat_gra',
            field=models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='lat_hem',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='lat_min',
            field=models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='lat_seg',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='lon_hem',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='lon_min',
            field=models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True),
        ),
    ]