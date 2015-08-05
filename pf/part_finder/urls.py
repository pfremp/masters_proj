__author__ = 'patrickfrempong'

from django.conf.urls import patterns, url, include
from part_finder import views
from django.contrib import admin
from registration.backends.simple.views import RegistrationView
from part_finder.forms import PartDemoForm,PartDetailsForm,PartStudentForm,PartPrefForm
from part_finder.views import  ParticipantRegistration, show_message_form_condition, ParticipantUpdate, ResearcherUpdate, process_application
from django.views.generic.edit import UpdateView
from part_finder.models import Participant
from django.contrib.auth.decorators import login_required
# from django.views.generic.simple import direct_to_template
# from .forms import NonAdminAddAnotherModelForm
# from .models import NonAdminAddAnotherModel
import autocomplete_light.shortcuts as al
from django.views import generic



participant_forms = [PartDetailsForm,PartStudentForm,PartDemoForm,PartPrefForm]

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add_experiment/$', views.add_experiment, name='add_experiment'),

    # url(r'^participant_details', views.participant_details, name='participant_details'),
    url(r'^experiments/(?P<r_slug>[\w\-]+)/(?P<experiment_name_slug>[\w\-]+)/$', views.experiment, name='experiment'),
    # url(r'^experiments/(?P<experiment_name_slug>[\w\-]+)/$', views.experiment, name='experiment'),
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
    url(r'^process_applications/(?P<r_slug>[\w\-]+)/(?P<experiment_name_slug>[\w\-]+)/$', views.process_application, name='process_applications'),
    url(r'^update_status/(?P<exp_id>[\w\-]+)/(?P<app_id>[\w\-]+)/$', views.update_application_status, name='update_application_status'),
    url(r'^current_experiments/$', views.researcher_experiments, name='researcher_experiments'),
    url(r'^delete/experiment/(?P<experiment_id>[\w\-]+)/$', views.delete_experiment, name='experiment-delete'),
    url(r'^profile/researcher/(?P<username>[\w\-]+)/$', views.researcher_profile, name='researcher_profile'),
    url(r'^experiments/$', views.all_experiments, name='allexperiments'),


    #test urls
    url(r'^todo/$', views.todo, name='todo'),
    # url(r'^dummy/$', views.dummy, name='dummy'),

    #
    # url(r'$', al.CreateView.as_view(
    #     model=NonAdminAddAnotherModel, form_class=NonAdminAddAnotherModelForm),
    #     name='non_admin_add_another_model_create'),
    # url(r'(?P<pk>\d+)/$', generic.UpdateView.as_view(
    #     model=NonAdminAddAnotherModel, form_class=NonAdminAddAnotherModelForm),
    #     name='non_admin_add_another_model_update'),
)


# url(r'^myobject/update/(?P<pk>\w+)/$' UpdateView.as_view(model=myModel, template_name="myupdate.html")) - See more at: http://glitterbug.in/blog/django-class-based-generic-views-the-good-the-bad-/show/#sthash.wehZtdWJ.dpuf