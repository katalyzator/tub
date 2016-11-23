# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from main.helper import transform

pathNews = 'news/images'
pathEvents = 'events/images'
pathPhoto = 'photos/images'
pathSlide = 'slider/images'


class SliderImage(models.Model):
    class Meta:
        verbose_name_plural = 'Картинки слайдера'
        verbose_name = 'Картинки слайдера'

    name = models.CharField(max_length=255)
    slideImage = models.ImageField(upload_to=transform(pathSlide))


class News(models.Model):
    class Meta:
        verbose_name_plural = 'Добавление новостей'
        verbose_name = 'Добавление новостей'

    title = models.CharField(max_length=255, verbose_name='Заголовок поста')
    description = models.CharField(max_length=1000, verbose_name='Описание поста')
    text = models.TextField(verbose_name='Текст поста')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/news/%i/" % self.id


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

    title = models.CharField(max_length=255, verbose_name='Заголовок поста')
    description = models.CharField(max_length=1000, verbose_name='Описание поста')
    text = models.TextField(verbose_name='Текст поста')

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
