from django.contrib import admin

# Register your models here.
from main.models import News, NewsImage, Event, EventImage, Photo, SliderImage


class NewsAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']
    list_display = ['title']
    list_filter = ['title', 'timestamp']
    readonly_fields = ['updated', 'timestamp']

    class Meta:
        model = News


class EventAdmin(admin.ModelAdmin):
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
