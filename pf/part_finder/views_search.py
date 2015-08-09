__author__ = 'patrickfrempong'
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, request
from part_finder.models import Researcher, Experiment, Participant, UserProfile, Contact, User,Dummy, Payment, Application, TimeSlot
from part_finder.forms import ExperimentForm, ResearcherForm, PartDetailsForm, ParticipantForm, SignupForm, TodoList, TimeSlotForm, TimeSlotFrom, PaymentForm, ApplicationForm, UpdateStatusForm, UpdateStatusFormFull
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# from django.contrib.formtools.wizard.views import SessionWizardView
from formtools.wizard.views import WizardView, SessionWizardView
from django.views.generic.edit import UpdateView, DeleteView
from part_finder.forms_search import *
from django.forms.formsets import formset_factory, BaseFormSet
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
import sys
import  datetime


# if experiment is matched, researcher will be
# redirected to complete the specific matched details.
@login_required
def matched_experiment(request, experiment_id):

    researcher = request.user.profile.researcher
    experiment = Experiment.objects.get(id=experiment_id, researcher=researcher)
    requirement = Requirement.objects.get(experiment=experiment)
    r_gender = requirement.gender
    r_age = requirement.age
    r_height = requirement.height
    r_weight = requirement.weight
    r_language = requirement.language

    if request.method == 'POST':

        match_form = MatchingDetailForm(request.POST)

        if match_form.is_valid():
            match_detail = match_form.save(commit=False)
            match_detail.requirement = requirement
            match_detail.save()
            return HttpResponseRedirect("/part_finder/")
        else:
            print match_form.errors

    else:
        match_form = MatchingDetailForm()



    context_dict = {'requirement': requirement, 'match_form': match_form, 'r_gender': r_gender, 'r_age': r_age, 'r_height':r_height, 'r_weight': r_weight, 'r_language': r_language}

    return render(request, 'part_finder/matched_experiment.html', context_dict)


def check_applicant_validity(request, experiment):
    valid = 0
    participant = request.user.profile.participant
    requirement = Requirement.objects.get(experiment=experiment)

    if requirement.gender == '1':

        if match_gender(request,experiment) == True:
            valid += 0
        else:
            valid += 1

    # if requirement.student == '1':
    #
    #     if match_student(request) == True:
    #         valid +=0
    #     else:
    #         valid +=1
    #
    # if requirement.age == '1':
    #     if match_age(request,experiment) == True:
    #         valid += 0
    #     else:
    #         valid += 1
    #
    # if requirement.language == '1':
    #     if match_lang(request, experiment) == True:
    #         valid += 0
    #     else:
    #         valid += 1
    #
    # if requirement.height == '1':
    #     if match_height(request, experiment):
    #         valid += 0
    #     else:
    #         valid += 1
    #
    # if requirement.weight == '1':
    #     if match_weight(request, experiment):
    #         valid += 0
    #     else:
    #         valid += 1

    return valid

def match_gender(request, experiment):

    try:
        participant = request.user.profile.participant
        requirement = Requirement.objects.get(experiment=experiment)
        match_details = MatchingDetail.objects.get(requirement=requirement)
        gender = match_details.gender

        if participant.gender.lower() == gender.lower():
            return True
        else:
            return False

    except User.DoesNotExist:
        pass


#
# def match_student(request):
#
#     try:
#         participant = request.user.profile.participant
#
#         if participant.student == True:
#             return True
#         else:
#             return False
#
#     except User.DoesNotExist:
#         pass
#
#
# def match_age(request, experiment):
#
#     try:
#         participant = request.user.profile.participant
#         requirement = Requirement.objects.get(experiment=experiment)
#         match_details = MatchingDetail.objects.get(requirement=requirement)
#
#         min_years = match_details.min_age
#         max_years = match_details.min_age
#         date = datetime.date.today()
#         min_age_date = date - (datetime.timedelta(days=min_years*365.25))
#         max_age_date = date - (datetime.timedelta(days=max_years*365.25))
#         participant_age = participant.dob
#
#         if participant_age <= min_age_date and participant_age >= max_age_date:
#             return True
#         else:
#             return False
#
#     except User.DoesNotExist:
#         pass
#
#
#
# def match_lang(request, experiment):
#
#     participant = request.user.profile.participant
#     experiment = experiment
#     requirement = Requirement.objects.get(experiment=experiment)
#     match_details = MatchingDetail.objects.get(requirement=requirement)
#
#     alllanguages = match_details.l
#     experiment_languages = alllanguages.split()
#
#     lang_req = False
#
#     for p_lang in participant.language:
#
#         if any(p_lang in l for l in experiment_languages):
#             lang_req = True
#
#     return lang_req
#
#
# def match_height(request, experiment):
#
#     try:
#         participant = request.user.profile.participant
#         experiment = experiment
#         requirement = Requirement.objects.get(experiment=experiment)
#         match_details = MatchingDetail.objects.get(requirement=requirement)
#
#         min_height_req = match_details.min_height
#         max_height_req = match_details.max_height
#
#         height_req = False
#
#         if participant.height > min_height_req and participant.height < max_height_req:
#             height_req = True
#
#         return height_req
#
#     except User.DoesNotExist:
#         pass
#
#
# def match_weight(request, experiment):
#
#     try:
#         participant = request.user.profile.participant
#         experiment = experiment
#         requirement = Requirement.objects.get(experiment=experiment)
#         match_details = MatchingDetail.objects.get(requirement=requirement)
#
#         min_weight_req = match_details.min_weight
#         max_weight_req = match_details.max_weight
#
#         weight_req = False
#
#         if participant.height > min_weight_req and participant.height < max_weight_req:
#             weight_req = True
#
#         return weight_req
#
#     except User.DoesNotExist:
#         pass



# # checks to see whether a participant is a student
# def check_for_student(participant_id):
#     part = Participant.objects.get(id=participant_id)
#
#     if part.student == True:
#         return True
#     else:
#         return False
