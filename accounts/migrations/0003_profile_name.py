# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-11 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180510_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='', max_length=80),
        ),
    ]