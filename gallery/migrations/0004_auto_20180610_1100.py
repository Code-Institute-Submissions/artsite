# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-10 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20180610_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about_me',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='facebook_url',
            field=models.URLField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fav_artist',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='medium',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='profile',
            name='occupation',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter_url',
            field=models.URLField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='website',
            field=models.URLField(blank=True, max_length=100),
        ),
    ]
