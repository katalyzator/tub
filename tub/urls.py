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
                                   url(r'^news/(?P<id>\d+)/$', 'main.views.singleNews', name='single_news'),
                                   url(r'^photos/', 'main.views.more_photos', name='photos'),
                                   url(r'^spor/', 'main.views.spor_views', name='spor')
                                   )

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
