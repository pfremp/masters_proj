__author__ = 'patrickfrempong'

from django.conf.urls import patterns, url
from part_finder import views

urlpatterns = ('',
               url(r'^$', views.index, name='index'))