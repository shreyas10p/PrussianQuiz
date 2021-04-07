# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2021-04-06 23:49
from __future__ import unicode_literals

import businesscard.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businesscard', '0006_auto_20210401_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, storage=businesscard.storage.PrivateMediaStorage(), upload_to=''),
        ),
    ]
