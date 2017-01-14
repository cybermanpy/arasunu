# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-11 22:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stationtypes', '0001_initial'),
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Climatology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_estacion', models.CharField(blank=True, max_length=60, null=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('tmax', models.CharField(blank=True, max_length=10, null=True)),
                ('tmin', models.CharField(blank=True, max_length=10, null=True)),
                ('tmed', models.CharField(blank=True, max_length=10, null=True)),
                ('td', models.CharField(blank=True, max_length=10, null=True)),
                ('pres_est', models.CharField(blank=True, max_length=10, null=True)),
                ('pres_mar', models.CharField(blank=True, max_length=10, null=True)),
                ('prcp', models.CharField(blank=True, max_length=10, null=True)),
                ('hr', models.CharField(blank=True, max_length=10, null=True)),
                ('helio', models.CharField(blank=True, max_length=10, null=True)),
                ('nub', models.CharField(blank=True, max_length=10, null=True)),
                ('vmax_d', models.CharField(blank=True, max_length=10, null=True)),
                ('vmax_f', models.CharField(blank=True, max_length=10, null=True)),
                ('vmed', models.CharField(blank=True, max_length=10, null=True)),
                ('id_estacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.Location')),
                ('id_tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stationtypes.StationType')),
            ],
            options={
                'verbose_name': 'Climatolog\xeda',
                'verbose_name_plural': 'Climatologias',
            },
        ),
    ]
