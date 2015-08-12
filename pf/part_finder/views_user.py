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
from part_finder.forms_search import RequirementForm
from part_finder.forms_user import *
from part_finder.views_search import *
from part_finder.views import index
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist




#all views associated with participant and researcher





#participant registrations
#after account signup, participant is redirected here to complete their participant profile
def participant_registration_1(request):
    if request.user.profile.participant == None:
        if request.method == 'POST':
            part_form = ParticipantForm1(request.POST)
            if request.user.profile.typex == 'Participant':
                if part_form.is_valid():
                    par = part_form.save()
                    profile = request.user.profile
                    profile.participant = par
                    profile.save()
                    return redirect("participant_registration_2")
                else:
                    print part_form.errors
        else:
            part_form = ParticipantForm1()
    else:
        return redirect("index")
    return render(request, 'part_finder/participant_registration_1.html', {'form': part_form})



# participant form 2
# collects detailed participant data
def participant_registration_2(request):
    # participant = Participant.objects.get_or_create(id=p_id)
    participant = request.user.profile.participant
    if participant.reg_2_completed == False:
        form = ParticipantForm2(request.POST or None, instance=participant)
        if form.is_valid():
            form.save()
            participant.reg_2_completed = True
            participant.save()
            return redirect("participant_profile")
        else:
            print form.errors
    else:
        return redirect("participant_profile")

    context_dict = {'form': form, 'part': participant}

    return render(request, 'part_finder/participant_registration_2.html', context_dict)



#Participant views

@login_required
#profile page
def profile_page(request):
    context_dict = {}
    participant = request.user.profile.participant
    lang = participant.language.all()
    user = request.user

    context_dict = {'participant': participant, 'lang': lang, 'user': user}

    return render (request, 'part_finder/profile.html', context_dict)


#Participant general details update
class UserAccountUpdate(UpdateView):

    model = User
    form_class = UserAccountUpdateForm
    template_name = 'part_finder/participant_update_form.html'
    success_url='/part_finder/participant/profile'

    def get_object(self, queryset=None):
        return self.request.user.profile.participant


#Participant general details update
class ParticipantGeneralUpdate(UpdateView):

    model = Participant
    form_class = PartGeneralUpdateForm
    template_name = 'part_finder/participant_update_form.html'
    success_url='/part_finder/participant/profile'

    def get_object(self, queryset=None):
        return self.request.user.profile.participant


#Participant student details update
class ParticipantStudentUpdate(UpdateView):

    model = Participant
    # form_class = PartStudentUpdateForm
    fields = ['university', 'course_name', 'year', 'matric' ]
    template_name = 'part_finder/participant_update_form.html'
    success_url='/part_finder/participant/profile'

    def get_object(self, queryset=None):
        return self.request.user.profile.participant


#Participant demo details update
class ParticipantDemoUpdate(UpdateView):

    model = Participant
    form_class = PartDemoUpdateForm
    template_name = 'part_finder/participant_update_form.html'
    success_url='/part_finder/participant/profile'

    def get_object(self, queryset=None):
        return self.request.user.profile.participant


#Participant preferences details update
class ParticipantPrefUpdate(UpdateView):

    model = Participant
    form_class = PartPrefUpdateForm
    template_name = 'part_finder/participant_update_form.html'
    success_url='/part_finder/participant/settings'

    def get_object(self, queryset=None):
        return self.request.user.profile.participant



@login_required
#user settings page
def settings_page(request):
    context_dict = {}
    participant = request.user.profile.participant


    context_dict = {'participant': participant, }

    return render (request, 'part_finder/settings.html', context_dict)


