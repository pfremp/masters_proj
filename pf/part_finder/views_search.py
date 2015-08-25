__author__ = 'patrickfrempong'
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, request
from part_finder.models import Researcher, Experiment, Participant, UserProfile, User, Payment, Application, TimeSlot
from part_finder.forms import ExperimentForm, TodoList, TimeSlotForm, PaymentForm, ApplicationForm, UpdateStatusForm, UpdateStatusFormFull
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

# Retrieve active participant user
def get_participant(request):
    try:
        if request.user.is_authenticated():
            participant = request.user.profile.participant
            return participant
    except User.is_anonymous:
        pass


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


# Check applicant validity
def check_applicant_validity(request, experiment):
    valid = 0

    participant = get_participant(request)
    try:
        requirement = Requirement.objects.get(experiment=experiment)

        # check gender
        if requirement.gender == '1':

            if match_gender(request,experiment) == True:
                valid += 0
            else:
                valid += 1

        # check student status
        if requirement.student == '1':

            if match_student(request) == True:
                valid +=0
            else:
                valid +=1

        # check age
        if requirement.age == '1':
            if match_age(request,experiment) == True:
                valid += 0
            else:
                valid += 1

        # check language
        if requirement.language == '1':
            if match_lang(request, experiment) == True:
                valid += 0
            else:
                valid += 1

        # check height
        if requirement.height == '1':
            if match_height(request, experiment):
                valid += 0
            else:
                valid += 1

        # check weight
        if requirement.weight == '1':
            if match_weight(request, experiment):
                valid += 0
            else:
                valid += 1

    except Requirement.DoesNotExist:
        requirement = None

    return valid



#participant preferences matching
def participant_pref_filter(request, experiment):
    valid = 0
    participant = get_participant(request)
    payment = Payment.objects.get(experiment=experiment)
    eligible = check_applicant_validity(request, experiment)

    #check for online exps - only show online experiments
    if participant.online_only == True:
        if experiment.online == True:
            valid += 0
        else:
            valid += 1

    # check for paid only experiments - only show paid experiments
    if participant.paid_only == True:

        if str(payment.is_paid) == 'Yes':

            valid += 0
        else:
            valid += 1

    # check for university status - only show experiments from participants university
    if participant.my_uni_only == True:
        if experiment.researcher.university == participant.university:
            valid += 0
        else:
            valid += 1

    # check for city only - only show experiemnts from the participant's city
    if participant.city_only == True:
        if experiment.city ==  participant.city:
            valid += 0
        else:
            valid += 1

    # check for eligibility - only show experiments that participant is eligible for
    if participant.eligible_only == True:
        if eligible == 0:
            valid += 0
        else:
            valid += 1

    return valid


# check if gender matches experiment gender
def match_gender(request, experiment):

    try:
        participant = get_participant(request)
        requirement = Requirement.objects.get(experiment=experiment)
        match_details = MatchingDetail.objects.get(requirement=requirement)
        gender = match_details.gender

        if participant.gender.lower() == gender.lower():
            return True
        else:
            return False

    except (User.DoesNotExist , MatchingDetail.DoesNotExist , Requirement.DoesNotExist), e:
        pass


# check if participant is a student
def match_student(request):

    try:
        participant = request.user.profile.participant

        if participant.student == True:
            return True
        else:
            return False

    except (User.DoesNotExist , MatchingDetail.DoesNotExist , Requirement.DoesNotExist), e:
        pass

# check is participant age meets the requirements
def match_age(request, experiment):

    try:
        participant = request.user.profile.participant
        requirement = Requirement.objects.get(experiment=experiment)
        match_details = MatchingDetail.objects.get(requirement=requirement)

        min_years = match_details.min_age
        max_years = match_details.max_age
        date = datetime.date.today()
        min_age_date = date - (datetime.timedelta(days=min_years*365.25))
        max_age_date = date - (datetime.timedelta(days=max_years*365.25))
        participant_age = participant.dob

        if participant_age <= min_age_date and participant_age >= max_age_date:
            return True
        else:
            return False

    except (User.DoesNotExist , MatchingDetail.DoesNotExist , Requirement.DoesNotExist), e:
        pass


# check if the participant has the required languages
def match_lang(request, experiment):

    participant = request.user.profile.participant
    experiment = experiment

    try:
        requirement = Requirement.objects.get(experiment=experiment)
        match_details = MatchingDetail.objects.get(requirement=requirement)
        participant_languages = participant.language.all()
        experiment_languages = match_details.l.replace('[','').replace('u','').replace("'",'').replace(']','').replace(',','')
        exp_lang = experiment_languages.split()

        v = 0

        for p in participant_languages:
            for e in exp_lang:
                if p.language.lower() == e.lower():
                    v += 1

        if v == len(exp_lang):
            return True

    except (MatchingDetail.DoesNotExist, Requirement.DoesNotExist) , e:
        match_details = None
        requirement = None


# check if the participant meets the height requirements
def match_height(request, experiment):

    try:
        participant = request.user.profile.participant
        experiment = experiment
        requirement = Requirement.objects.get(experiment=experiment)
        match_details = MatchingDetail.objects.get(requirement=requirement)

        min_height_req = match_details.min_height
        max_height_req = match_details.max_height

        height_req = False

        if participant.height > min_height_req and participant.height < max_height_req:
            height_req = True

        return height_req

    except (User.DoesNotExist , MatchingDetail.DoesNotExist , Requirement.DoesNotExist), e:
        pass


# check if participant has the correct weight
def match_weight(request, experiment):

    try:
        participant = request.user.profile.participant
        experiment = experiment
        requirement = Requirement.objects.get(experiment=experiment)
        match_details = MatchingDetail.objects.get(requirement=requirement)

        min_weight_req = match_details.min_weight
        max_weight_req = match_details.max_weight

        weight_req = False

        if participant.height > min_weight_req and participant.height < max_weight_req:
            weight_req = True

        return weight_req

    except (User.DoesNotExist , MatchingDetail.DoesNotExist , Requirement.DoesNotExist), e:
        pass

