# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-12 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20180610_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='stripe_id',
            field=models.CharField(default='', max_length=40),
        ),
    ]