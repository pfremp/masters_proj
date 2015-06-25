from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings # New Import
from django.conf.urls.static import static # New Import




urlpatterns = patterns('',

url(r'^admin/', include(admin.site.urls)),
url(r'^part_finder/', include('part_finder.urls')),

)

if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )