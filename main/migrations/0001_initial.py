# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-07 19:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430')),
                ('title_tr', models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430')),
                ('title_az', models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430')),
                ('title_kz', models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430')),
                ('description', models.CharField(max_length=1000, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430')),
                ('description_ru', models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430')),
                ('description_en', models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430')),
                ('description_tr', models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430')),
                ('description_az', models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430')),
                ('description_kz', models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430')),
                ('text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430')),
                ('text_ru', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430')),
                ('text_en', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430')),
                ('text_tr', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430')),
                ('text_az', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430')),
                ('text_kz', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 activity1',
                'verbose_name_plural': '\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 activity1',
            },
        ),
        migrations.CreateModel(
            name='Activity2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430')),
                ('title_tr', models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430')),
                ('title_az', models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430')),
                ('title_kz', models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430')),
                ('description', models.CharField(max_length=1000, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430')),
                ('description_ru', models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430')),
                ('description_en', models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430')),
                ('description_tr', models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430')),
                ('description_az', models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430')),
                ('description_kz', models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430')),
                ('text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430')),
                ('text_ru', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430')),
                ('text_en', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430')),
                ('text_tr', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430')),
                ('text_az', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430')),
                ('text_kz', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 activity2',
                'verbose_name_plural': '\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 activity2',
            },
        ),
        migrations.CreateModel(
            name='Activity3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430')),
                ('title_tr', models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430')),
                ('title_az', models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430')),
                ('title_kz', models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430')),
                ('description', models.CharField(max_length=1000, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430')),
                ('description_ru', models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430')),
                ('description_en', models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430')),
                ('description_tr', models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430')),
                ('description_az', models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430')),
                ('description_kz', models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430')),
                ('text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430')),
                ('text_ru', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430')),
                ('text_en', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430')),
                ('text_tr', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430')),
                ('text_az', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430')),
                ('text_kz', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 activity3',
                'verbose_name_plural': '\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 activity3',
            },
        ),
        migrations.CreateModel(
            name='ActivityImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='\u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0430')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Activity', verbose_name='\u0432\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0438 activity1',
                'verbose_name_plural': '\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0438 activity1',
            },
        ),
        migrations.CreateModel(
            name='ActivityImage2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='\u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0430')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Activity2', verbose_name='\u0432\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0438 activity2',
                'verbose_name_plural': '\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0438 activity2',
            },
        ),
        migrations.CreateModel(
            name='ActivityImage3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='\u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0430')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Activity3', verbose_name='\u0432\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0438 activity3',
                'verbose_name_plural': '\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0438 activity3',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430')),
                ('title_tr', models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430')),
                ('title_az', models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430')),
                ('title_kz', models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430')),
                ('description', models.CharField(max_length=1000, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430')),
                ('description_ru', models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430')),
                ('description_en', models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430')),
                ('description_tr', models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430')),
                ('description_az', models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430')),
                ('description_kz', models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430')),
                ('text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430')),
                ('text_ru', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430')),
                ('text_en', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430')),
                ('text_tr', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430')),
                ('text_az', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430')),
                ('text_kz', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0439',
                'verbose_name_plural': '\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0439',
            },
        ),
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='\u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0430')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Event', verbose_name='\u0432\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0438 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0439',
                'verbose_name_plural': '\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0438 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0439',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430')),
                ('title_tr', models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430')),
                ('title_az', models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430')),
                ('title_kz', models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430')),
                ('description', models.CharField(max_length=1000, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430')),
                ('description_ru', models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430')),
                ('description_en', models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430')),
                ('description_tr', models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430')),
                ('description_az', models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430')),
                ('description_kz', models.CharField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430')),
                ('text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430')),
                ('text_ru', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430')),
                ('text_en', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430')),
                ('text_tr', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430')),
                ('text_az', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430')),
                ('text_kz', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u0442\u0430')),
                ('urls', models.URLField(blank=True, verbose_name='URL')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0441\u0442\u0435\u0439',
                'verbose_name_plural': '\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0441\u0442\u0435\u0439',
            },
        ),
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='\u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0430')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.News', verbose_name='\u0432\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043d\u043e\u0432\u043e\u0441\u0442\u044c')),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0438 \u043d\u043e\u0432\u043e\u0441\u0442\u0435\u0439',
                'verbose_name_plural': '\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0438 \u043d\u043e\u0432\u043e\u0441\u0442\u0435\u0439',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('file', models.ImageField(upload_to='', verbose_name='\u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438',
                'verbose_name_plural': '\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slideImage', models.ImageField(upload_to='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0438 \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u0430',
                'verbose_name_plural': '\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0438 \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u0430',
            },
        ),
    ]
