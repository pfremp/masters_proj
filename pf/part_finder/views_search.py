__author__ = 'patrickfrempong'
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, request
from part_finder.models import Researcher, Experiment, Participant, UserProfile, User, Payment, Application, TimeSlot
from part_finder.forms import ExperimentForm, TimeSlotForm, PaymentForm, ApplicationForm, UpdateStatusForm, UpdateStatusFormFull
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# from django.contrib.formtools.wizard.views import SessionWizardView
from formtools.wizard.views import WizardView, SessionWizardView
from django.views.generic.edit import UpdateView, DeleteView
from part_finder.forms_search import *
from django.forms.formsets import formset_factory, BaseFormSet
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
import sys
import datetime


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
            return HttpResponseRedirect(reverse('index'))
        else:
            print match_form.errors

    else:
        match_form = MatchingDetailForm()

    context_dict = {'requirement': requirement, 'match_form': match_form, 'r_gender': r_gender,
                    'r_age': r_age, 'r_height':r_height, 'r_weight': r_weight, 'r_language': r_language}

    return render(request, 'part_finder/matched_experiment.html', context_dict)


# Check applicant validity
def check_applicant_validity(request, experiment):

    participant = get_participant(request)

    try:
        requirement = Requirement.objects.get(experiment=experiment)
        match_details = MatchingDetail.objects.get(requirement=requirement)
    except (Requirement.DoesNotExist, MatchingDetail.DoesNotExist):
        return True

    # check gender
    if requirement.gender and not match_gender(participant, match_details):
        return False

    # check student status
    if requirement.student and not participant.student:
        return False

    # check age
    if requirement.age and not match_age(participant,match_details):
        return False

    # check language
    if requirement.language and not match_lang(participant, match_details):
        return False

    # check height
    if requirement.height and not match_height(participant, match_details):
        return False

    # check weight
    if requirement.weight and not match_weight(participant, match_details):
        return False

    return True


# participant preferences matching
def participant_pref_filter(request, experiment):
    participant = get_participant(request)
    payment = Payment.objects.get(experiment=experiment)
    eligible = check_applicant_validity(request, experiment)
    applications = Application.objects.filter(participant=participant)

    #check for online exps - only show online experiments
    if participant.online_only and not experiment.online:
        return False

    # check for paid only experiments - only show paid experiments
    if participant.paid_only and str(payment.is_paid) != 'Yes':
        return False

    # check for university status - only show experiments from participants university
    if participant.my_uni_only and experiment.researcher.university != participant.university:
        return False

    # check for city only - only show experiemnts from the participant's city
    if participant.city_only and experiment.city != participant.city:
        return False

    # check for eligibility - only show experiments that participant is eligible for
    if participant.eligible_only and eligible != 0:
        return False

    # Don't show experiments that have already been applied for
    if participant.non_applied_only and (experiment in [a.experiment for a in applications]):
        return False

    return True


# check if gender matches experiment gender
def match_gender(participant, match_details):
    return participant.gender.lower() == match_details.gender.lower()


# check is participant age meets the requirements
def match_age(participant, match_details):
    min_years = match_details.min_age
    max_years = match_details.max_age

    print min_years
    print max_years
    date = datetime.date.today()
    min_age_date = date - (datetime.timedelta(days=min_years*365.25))
    max_age_date = date - (datetime.timedelta(days=max_years*365.25))

    participant_age = participant.dob

    print "Min Age Date " + str(min_age_date)
    print "DOB: " + str(participant_age)
    print "Max Age Date " + str(max_age_date)
    print "--" + str(participant_age <= min_age_date and participant_age >= max_age_date)

    return (participant_age <= min_age_date and participant_age >= max_age_date)


# check if the participant has the required languages
def match_lang(participant, match_details):
    participant_languages = participant.language.all()
    experiment_languages = match_details.l.replace('[','').replace('u','').replace("'",'').replace(']','').replace(',','')
    exp_lang = experiment_languages.split()

    # converts languages in participant languages list to lowercase and converts list to set
    participant_languages_lower = set([str(lang).lower() for lang in participant_languages])
    # converts languages in required languages list to lowercase and converts list to set
    required_languages_lower = set([lang.lower() for lang in exp_lang])

    return required_languages_lower.issubset(participant_languages_lower)


# check if the participant meets the height requirements
def match_height(participant, match_details):
    return participant.height >= match_details.min_height and participant.height <= match_details.max_height


# check if participant has the correct weight
def match_weight(participant, match_details):
    return participant.weight >= match_details.min_weight and participant.weight <= match_details.max_weight





