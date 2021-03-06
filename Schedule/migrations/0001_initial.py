# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-19 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='engagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engagementID', models.PositiveIntegerField()),
                ('client_name', models.CharField(max_length=255)),
                ('engagement_description', models.CharField(max_length=255)),
                ('engagement_code', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resourceID', models.PositiveIntegerField()),
                ('resource_name', models.CharField(max_length=255)),
                ('resource_level', models.CharField(max_length=255)),
                ('resource_firm', models.CharField(max_length=25)),
                ('resource_group', models.CharField(max_length=255)),
            ],
        ),
    ]
