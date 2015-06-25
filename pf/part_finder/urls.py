__author__ = 'patrickfrempong'

from django.conf.urls import patterns, url, include
from part_finder import views
from django.contrib import admin
from registration.backends.simple.views import RegistrationView

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add_experiment/$', views.add_experiment, name='add_experiment'),
    url(r'^participant_details', views.participant_details, name='participant_details'),
    url(r'^experiments/(?P<experiment_name_slug>[\w\-]+)/$', views.experiment, name='experiment'),
    url(r'^researcher_signup/$', views.researcher_signup, name='researcher_signup' ),


    )


