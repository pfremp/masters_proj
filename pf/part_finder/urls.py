__author__ = 'patrickfrempong'

from django.conf.urls import patterns, url, include
from part_finder import views, views_search, views_user
from django.contrib import admin
from registration.backends.simple.views import RegistrationView

from part_finder.views import process_application, ExperimentUpdate, PaymentUpdate, TimeSlotUpdate, RequirementUpdate, MatchDetailsUpdate
from part_finder.views_user import ParticipantGeneralUpdate, ParticipantStudentUpdate, ParticipantDemoUpdate, ParticipantPrefUpdate, ParticipantPrefUpdateNS,UserAccountUpdate, participant_registration_1, ResearcherUpdate

from django.views.generic.edit import UpdateView
from part_finder.models import Participant
from django.contrib.auth.decorators import login_required
# from django.views.generic.simple import direct_to_template
# from .forms import NonAdminAddAnotherModelForm
# from .models import NonAdminAddAnotherModel
import autocomplete_light.shortcuts as al
from django.views import generic
from part_finder.forms_user import ParticipantForm1



# participant_forms = [PartDetailsForm,PartStudentForm,PartDemoForm]

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login_success/$', views_user.login_success, name='login_success'),
    url(r'^participant/experiment_history/$', views_user.participant_experiment_history, name='participant_experiment_history'),
    url(r'^experiments/$', views.all_experiments, name='allexperiments'),

    #researcher
    url(r'^researcher_registration/$', views_user.researcher_registration, name='researcher_registration'),
    url(r'^researcher/update/$', login_required(ResearcherUpdate.as_view()), name='update_researcher_details'),
    url(r'^researcher/delete/experiment/(?P<experiment_id>[\w\-]+)/$', views.delete_experiment, name='experiment-delete'),
    url(r'^end_experiment/(?P<experiment_id>[\w\-]+)/$', views.end_experiment, name='end_experiment'),
    url(r'^reactivate_experiment/(?P<experiment_id>[\w\-]+)/$', views.reac_experiment, name='reac_experiment'),
    url(r'^process_applications/(?P<r_slug>[\w\-]+)/(?P<experiment_name_slug>[\w\-]+)/$', views.process_application, name='process_applications'),
    url(r'^update_status/(?P<exp_id>[\w\-]+)/(?P<app_id>[\w\-]+)/$', views.update_application_status, name='update_application_status'),
    url(r'^current_experiments/$', views_user.researcher_experiments, name='researcher_experiments'),
    url(r'^profile/researcher/(?P<username>[\w\-]+)/$', views_user.researcher_profile, name='researcher_profile'),

    #participant urls.
    url(r'^participant/profile/$', views_user.profile_page, name='participant_profile'),
    url(r'^participant/settings/$', views_user.settings_page, name='participant_settings'),
    url(r'^participant/profile/general/update/$', login_required(ParticipantGeneralUpdate.as_view()), name='update_participant_general'),
    url(r'^participant/profile/student/update/$', login_required(ParticipantStudentUpdate.as_view()), name='update_participant_student'),
    url(r'^participant/profile/demographic/update/$', login_required(ParticipantDemoUpdate.as_view()), name='update_participant_demo'),
    url(r'^participant/profile/preferences/update/$', login_required(ParticipantPrefUpdate.as_view()), name='update_participant_pref'),
    url(r'^participant/profile/preferences/update/$', login_required(ParticipantPrefUpdateNS.as_view()), name='update_participant_pref_ns'),
    url(r'^participant_registration_1/$', views_user.participant_registration_1, name='participant_registration_1'),
    url(r'^participant_registration_2/$', views_user.participant_registration_2, name='participant_registration_2'),
    url(r'^my_experiments/$', views_user.participant_experiments, name='participant_experiments'),
    url(r'^participant/delete/experiment/(?P<experiment_id>[\w\-]+)/$', views.delete_participant_experiment, name='delete_participant_experiment'),
    # url(r'^participant/profile/user/update/$', login_required(UserAccountUpdate.as_view()), name='update_user_account'),
    # url(r'^$', views.index, name='password_change_done'),
    # url(r'password_change/$', 'django.contrib.auth.views.password_change', {'template_name': 'part_finder/participant_update_form.html'}),

    #experiment urls
    url(r'^experiments/(?P<r_slug>[\w\-]+)/(?P<experiment_name_slug>[\w\-]+)/$', views.experiment, name='experiment'),
    url(r'^add_experiment/$', views.add_experiment, name='add_experiment'),
    url(r'^experiment/update/(?P<pk>[\w\-]+)/$', login_required(ExperimentUpdate.as_view()), name='update_experiment'),
    url(r'^experiment/update/(?P<pk>[\w\-]+)/$', login_required(ExperimentUpdate.as_view()), name='update_researcher_details'),
    url(r'^experiment/payment/update/(?P<pk>[\w\-]+)/(?P<slug>[\w\-]+)/$', login_required(PaymentUpdate.as_view()), name='update_payment'),
    url(r'^experiment/timeslot/(?P<experiment_id>[\w\-]+)/$', views.exp_timeslots, name='experiment_timeslots'),
    url(r'^experiment/timeslot/update/(?P<pk>[\w\-]+)/(?P<slug>[\w\-]+)/$', login_required(TimeSlotUpdate.as_view()), name='update_timeslot'),
    url(r'^experiment/requirement/update/(?P<pk>[\w\-]+)/(?P<slug>[\w\-]+)/$', login_required(RequirementUpdate.as_view()), name='update_requirement'),
    url(r'^experiment/requirement/details/update/(?P<pk>[\w\-]+)/(?P<slug>[\w\-]+)/$', login_required(MatchDetailsUpdate.as_view()), name='update_requirement_details'),
    url(r'^experiment_history/$', views.experiment_history, name='experiment-history'),
    url(r'^match/(?P<experiment_id>[\w\-]+)/$', views_search.matched_experiment, name='set_match'),

    url(r'^autocomplete/', include('autocomplete_light.urls')),

    #test urls
    # url(r'^todo/$', views.todo, name='todo'),
    # url(r'^masonary/$', views.masonary, name='masonary')
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