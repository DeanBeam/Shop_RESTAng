# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outlet', '0002_auto_20161118_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_cartElement',
            field=models.ManyToManyField(blank=True, to='outlet.CartElement'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_deep',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_height',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_liked',
            field=models.ManyToManyField(blank=True, to='outlet.UserProfile'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_weight',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_width',
            field=models.FloatField(blank=True),
        ),
    ]
