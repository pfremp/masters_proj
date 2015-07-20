__author__ = 'patrickfrempong'

from django.conf.urls import patterns, url, include
from part_finder import views
from django.contrib import admin
from registration.backends.simple.views import RegistrationView
from part_finder.forms import PartDemoForm,PartDetailsForm,PartStudentForm,PartPrefForm
from part_finder.views import  ParticipantRegistration, show_message_form_condition, ParticipantUpdate, ResearcherUpdate
from django.views.generic.edit import UpdateView
from part_finder.models import Participant
from django.contrib.auth.decorators import login_required
# from django.views.generic.simple import direct_to_template


participant_forms = [PartDetailsForm,PartStudentForm,PartDemoForm,PartPrefForm]

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add_experiment/$', views.add_experiment, name='add_experiment'),
    url(r'^dummy/$', views.dummy, name='dummy'),
    # url(r'^participant_details', views.participant_details, name='participant_details'),
    url(r'^experiments/(?P<experiment_name_slug>[\w\-]+)/$', views.experiment, name='experiment'),
    # url(r'^researcher_signup/$', views.researcher_signup, name='researcher_signup' ),
    # url(r'^complete_registration/$', views.complete_registration, name='complete_registration'),
    url(r'^login_success/$', views.login_success, name='login_success'),
    # url(r'^login_page/$', views.login_page, name='login_page'),
    url(r'^participant_registration/$', ParticipantRegistration.as_view(participant_forms, condition_dict = {'1': show_message_form_condition})),
    url(r'^researcher_registration/$', views.researcher_registration, name='researcher_registration'),
    url(r'^participant/update/$', login_required(ParticipantUpdate.as_view()), name='update_participant_details'),
    # url(r'^profile/update/$', login_required(ProfileUpdate.as_view()), name='update_profile'),
    url(r'^researcher/update/$', login_required(ResearcherUpdate.as_view()), name='update_researcher_details'),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
)


# url(r'^myobject/update/(?P<pk>\w+)/$' UpdateView.as_view(model=myModel, template_name="myupdate.html")) - See more at: http://glitterbug.in/blog/django-class-based-generic-views-the-good-the-bad-/show/#sthash.wehZtdWJ.dpuf