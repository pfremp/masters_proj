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


def matched_experiment(request, experiment_id):
    # context_dict = {}

    researcher = request.user.profile.researcher
    experiment = Experiment.objects.get(id=experiment_id, researcher=researcher)
    requirement = Requirement.objects.get(experiment=experiment)
    r_gender = requirement.gender
    r_age = requirement.age
    # r_max_age = requirement.age
    r_height = requirement.height
    r_weight = requirement.weight
    r_language = requirement.language


    # requirement = requirement
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


        #
        # age_form = AgeForm(request.POST)
        # height_form = HeightForm(request.POST)
        # weight_form = WeightForm(request.POST)
        #
        #      if gender_form.is_valid() and age_form.is_valid() and height_form.is_valid() and weight_form.is_valid():
        #         application = appform.save(commit=False)
        #         application.researcher = experiment.researcher
        #         application.participant = request.user.profile.participant
        #         application.experiment = experiment
        #         application.status = 'Pending'
        #         timeslot =  application.timeslot
        #         # timeslot.current_parts += 1
        #         # timeslot.save()
        #         application.save()
        #         return HttpResponseRedirect("/part_finder/")
        #
        #
        #      else:
        #         print appform.errors
        # # else:
        #      appform = ApplicationForm(experiment)


    return render(request, 'part_finder/matched_experiment.html', context_dict)




# def match_lang(participant):



#
#
#
# # checks to see whether a participant is a student
# def check_for_student(participant_id):
#     part = Participant.objects.get(id=participant_id)
#
#     if part.student == True:
#         return True
#     else:
#         return False
