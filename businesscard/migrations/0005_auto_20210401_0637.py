# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2021-04-01 06:37
from __future__ import unicode_literals

from django.db import migrations
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('businesscard', '0004_auto_20210401_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=s3direct.fields.S3DirectField(blank=True),
        ),
    ]
