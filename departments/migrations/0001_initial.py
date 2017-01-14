# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-11 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_dpto', models.CharField(max_length=100)),
                ('nombre_cap', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
        ),
    ]