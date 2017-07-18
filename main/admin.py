# coding=utf-8
from django.contrib import admin

# Register your models here.
from modeltranslation.admin import TabbedExternalJqueryTranslationAdmin
from main.models import NewsImage, Event, EventImage, Photo, SliderImage, Activity, ActivityImage

from modeltranslation.translator import TranslationOptions, translator
from main.models import News, Activity2, Activity3, ActivityImage2, ActivityImage3


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'text', 'content')


class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'text', 'content')


class ActivityTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'text')


class ActivityTranslationOptions2(TranslationOptions):
    fields = ('title', 'description', 'text')


class ActivityTranslationOptions3(TranslationOptions):
    fields = ('title', 'description', 'text')


translator.register(Event, EventTranslationOptions)

translator.register(News, NewsTranslationOptions)

translator.register(Activity, ActivityTranslationOptions)

translator.register(Activity2, ActivityTranslationOptions)

translator.register(Activity3, ActivityTranslationOptions)


class NewsAdmin(TabbedExternalJqueryTranslationAdmin):
    search_fields = ['title', 'description']
    list_display = ['title']
    list_filter = ['title', 'timestamp']
    readonly_fields = ['updated', 'timestamp']

    class Meta:
        model = News


class ActivityAdmin(TabbedExternalJqueryTranslationAdmin):
    search_fields = ['title', 'description']
    list_display = ['title']
    list_filter = ['title', 'timestamp']
    readonly_fields = ['updated', 'timestamp']

    class Meta:
        model = Activity


class ActivityAdmin2(TabbedExternalJqueryTranslationAdmin):
    search_fields = ['title', 'description']
    list_display = ['title']
    list_filter = ['title', 'timestamp']
    readonly_fields = ['updated', 'timestamp']

    class Meta:
        model = Activity2


class ActivityAdmin3(TabbedExternalJqueryTranslationAdmin):
    search_fields = ['title', 'description']
    list_display = ['title']
    list_filter = ['title', 'timestamp']
    readonly_fields = ['updated', 'timestamp']

    class Meta:
        model = Activity3


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

admin.site.register(Activity, ActivityAdmin)

admin.site.register(ActivityImage)

admin.site.register(Activity2, ActivityAdmin2)

admin.site.register(ActivityImage2)

admin.site.register(Activity3, ActivityAdmin3)

admin.site.register(ActivityImage3)

admin.site.register(Photo)

admin.site.register(SliderImage)
