# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-30 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testbank', '0002_auto_20170830_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='preround_end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='preround_start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
