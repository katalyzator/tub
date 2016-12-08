# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-24 06:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20161123_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='sliderimage',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 11, 24, 6, 27, 6, 594109, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sliderimage',
            name='updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 11, 24, 6, 27, 28, 458770, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
