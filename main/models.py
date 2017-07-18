# coding=utf-8
from __future__ import unicode_literals

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from main.helper import transform

pathNews = 'news/images'
pathEvents = 'events/images'
pathPhoto = 'photos/images'
pathSlide = 'slider/images'
pathActivity = 'activity/images'
pathActivity2 = 'activity2/images'
pathActivity3 = 'activity3/images'


class SliderImage(models.Model):
    class Meta:
        verbose_name_plural = 'Картинки слайдера'
        verbose_name = 'Картинки слайдера'

    name = models.CharField(max_length=255)
    slideImage = models.ImageField(upload_to=transform(pathSlide))

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name


class News(models.Model):
    class Meta:
        verbose_name_plural = 'Добавление новостей'
        verbose_name = 'Добавление новостей'

    title = models.CharField(max_length=255, verbose_name='Заголовок поста', blank=True)
    description = models.CharField(max_length=1000, verbose_name='Описание поста', blank=True)
    text = models.TextField(verbose_name='Текст поста', blank=True)
    content = RichTextUploadingField(verbose_name='контент новости')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/news/%i/" % self.id


class Activity(models.Model):
    class Meta:
        verbose_name_plural = 'Добавление activity1'
        verbose_name = 'Добавление activity1'

    title = models.CharField(max_length=255, verbose_name='Заголовок поста')
    description = models.CharField(max_length=1000, verbose_name='Описание поста')
    text = models.TextField(verbose_name='Текст поста')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/activity/%i/" % self.id


class ActivityImage(models.Model):
    class Meta:
        verbose_name_plural = 'Картинки activity1'
        verbose_name = 'Картинки activity1'

    activity = models.ForeignKey(Activity, verbose_name='выберите мероприятие')
    image = models.ImageField(upload_to=transform(pathActivity), verbose_name='картинка')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return str(self.id)


class Activity2(models.Model):
    class Meta:
        verbose_name_plural = 'Добавление activity2'
        verbose_name = 'Добавление activity2'

    title = models.CharField(max_length=255, verbose_name='Заголовок поста')
    description = models.CharField(max_length=1000, verbose_name='Описание поста')
    text = models.TextField(verbose_name='Текст поста')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/activity2/%i/" % self.id


class ActivityImage2(models.Model):
    class Meta:
        verbose_name_plural = 'Картинки activity2'
        verbose_name = 'Картинки activity2'

    activity = models.ForeignKey(Activity2, verbose_name='выберите мероприятие')
    image = models.ImageField(upload_to=transform(pathActivity2), verbose_name='картинка')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return str(self.id)


class Activity3(models.Model):
    class Meta:
        verbose_name_plural = 'Добавление activity3'
        verbose_name = 'Добавление activity3'

    title = models.CharField(max_length=255, verbose_name='Заголовок поста')
    description = models.CharField(max_length=1000, verbose_name='Описание поста')
    text = models.TextField(verbose_name='Текст поста')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/activity3/%i/" % self.id


class ActivityImage3(models.Model):
    class Meta:
        verbose_name_plural = 'Картинки activity3'
        verbose_name = 'Картинки activity3'

    activity = models.ForeignKey(Activity3, verbose_name='выберите мероприятие')
    image = models.ImageField(upload_to=transform(pathActivity3), verbose_name='картинка')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return str(self.id)


class NewsImage(models.Model):
    class Meta:
        verbose_name_plural = 'Картинки новостей'
        verbose_name = 'Картинки новостей'

    news = models.ForeignKey(News, verbose_name='выберите новость')
    image = models.ImageField(upload_to=transform(pathNews), verbose_name='картинка')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return str(self.id)


class Event(models.Model):
    class Meta:
        verbose_name_plural = 'Добавление мероприятий'
        verbose_name = 'Добавление мероприятий'

    title = models.CharField(max_length=255, verbose_name='Заголовок поста', blank=True)
    description = models.CharField(max_length=1000, verbose_name='Описание поста', blank=True)
    text = models.TextField(verbose_name='Текст поста', blank=True)

    content = RichTextUploadingField(verbose_name='контент новости')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/events/%i/" % self.id


class EventImage(models.Model):
    class Meta:
        verbose_name_plural = 'Картинки мероприятий'
        verbose_name = 'Картинки мероприятий'

    event = models.ForeignKey(Event, verbose_name='выберите мероприятие')
    image = models.ImageField(upload_to=transform(pathEvents), verbose_name='картинка')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return str(self.id)


class Photo(models.Model):
    class Meta:
        verbose_name_plural = 'Фотографии'
        verbose_name = 'Фотографии'

    name = models.CharField(max_length=100, blank=True)
    file = models.ImageField(upload_to=transform(pathPhoto), verbose_name='фотография')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name
