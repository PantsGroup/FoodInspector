# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 20:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=20)),
                ('inspection_date', models.CharField(max_length=30)),
                ('inspection_score', models.IntegerField()),
                ('violation', models.TextField(max_length=1000)),
                ('risk_category', models.CharField(max_length=100)),
            ],
        ),
    ]
