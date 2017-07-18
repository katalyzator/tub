from django.conf.urls import url, patterns, include
from django.contrib import admin
from django.conf.urls.static import static
from solid_i18n.urls import solid_i18n_patterns

from tub import settings

urlpatterns = []

urlpatterns += solid_i18n_patterns('',
                                   url(r'^jet/', include('jet.urls', 'jet')),
                                   url(r'^admin/', admin.site.urls),
                                   url(r'^$', 'main.views.index_view', name='index'),
                                   url(r'^ckeditor/', include('ckeditor_uploader.urls')),
                                   url(r'^news/(?P<id>\d+)/$', 'main.views.singleNews', name='single_news'),
                                   url(r'^events/(?P<id>\d+)/$', 'main.views.singleEvents', name='single_event'),
                                   url(r'^activity/(?P<id>\d+)/$', 'main.views.singleActivity1', name='activity1'),
                                   url(r'^activity2/(?P<id>\d+)/$', 'main.views.singleActivity2', name='activity2'),
                                   url(r'^activity3/(?P<id>\d+)/$', 'main.views.singleActivity3', name='activity3'),
                                   url(r'^photos1/', 'main.views.more_photos', name='photos1'),
                                   url(r'^photos2/', 'main.views.more_photos2', name='photos2'),
                                   url(r'^photos3/', 'main.views.more_photos3', name='photos3'),
                                   url(r'^activities/', 'main.views.activity_news1', name='activity_1'),
                                   url(r'^activities2/', 'main.views.activity_news2', name='activity_2'),
                                   url(r'^activities3/', 'main.views.activity_news3', name='activity_3'),
                                   url(r'^news/', 'main.views.all_news_view', name='all_news_view'),
                                   url(r'^events/', 'main.views.all_events_view', name='all_events_view'),
                                   url(r'^orhun/', 'main.views.orhun_view', name='orhun'),
                                   )

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
