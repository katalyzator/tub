# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-19 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170216_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='description_az',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='activity',
            name='description_kz',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='activity',
            name='text_az',
            field=models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='activity',
            name='text_kz',
            field=models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='activity',
            name='title_az',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='activity',
            name='title_kz',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='activity2',
            name='description_az',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='activity2',
            name='description_kz',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='activity2',
            name='text_az',
            field=models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='activity2',
            name='text_kz',
            field=models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='activity2',
            name='title_az',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='activity2',
            name='title_kz',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='activity3',
            name='description_az',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='activity3',
            name='description_kz',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='activity3',
            name='text_az',
            field=models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='activity3',
            name='text_kz',
            field=models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='activity3',
            name='title_az',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='activity3',
            name='title_kz',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='event',
            name='description_az',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='event',
            name='description_kz',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='event',
            name='text_az',
            field=models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='event',
            name='text_kz',
            field=models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='event',
            name='title_az',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='event',
            name='title_kz',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='news',
            name='description_az',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='news',
            name='description_kz',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='news',
            name='text_az',
            field=models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='news',
            name='text_kz',
            field=models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_az',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_kz',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430'),
        ),
    ]
