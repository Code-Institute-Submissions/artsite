# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-10 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0002_auto_20180610_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
