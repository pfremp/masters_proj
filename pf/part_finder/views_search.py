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

from django.forms.formsets import formset_factory, BaseFormSet
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
import sys


def search



# checks to see whether a participant is a student
def check_for_student(participant_id):
    part = Participant.objects.get(id=participant_id)

    if part.student == True:
        return True
    else:
        return False
