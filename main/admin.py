# coding=utf-8
from django.contrib import admin

# Register your models here.
from modeltranslation.admin import TabbedExternalJqueryTranslationAdmin
from main.models import News, NewsImage, Event, EventImage, Photo, SliderImage

from modeltranslation.translator import TranslationOptions, translator
from main.models import News


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'text')


class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'text')

translator.register(Event, EventTranslationOptions)

translator.register(News, NewsTranslationOptions)


class NewsAdmin(TabbedExternalJqueryTranslationAdmin):
    search_fields = ['title', 'description']
    list_display = ['title']
    list_filter = ['title', 'timestamp']
    readonly_fields = ['updated', 'timestamp']


class EventAdmin(TabbedExternalJqueryTranslationAdmin):
    search_fields = ['title', 'description']
    list_display = ['title']
    list_filter = ['title', 'timestamp']
    readonly_fields = ['updated', 'timestamp']

    class Meta:
        model = Event


admin.site.register(News, NewsAdmin)

admin.site.register(NewsImage)

admin.site.register(Event, EventAdmin)

admin.site.register(EventImage)

admin.site.register(Photo)

admin.site.register(SliderImage)
