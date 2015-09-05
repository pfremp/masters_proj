__author__ = 'patrickfrempong'
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, request
from part_finder.models import Researcher, Experiment, Participant, UserProfile, User, Payment, Application, TimeSlot
from part_finder.forms import ExperimentForm,  TimeSlotForm, PaymentForm, ApplicationForm, UpdateStatusForm, UpdateStatusFormFull
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from formtools.wizard.views import WizardView, SessionWizardView
from django.views.generic.edit import UpdateView, DeleteView

from django.forms.formsets import formset_factory, BaseFormSet
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
import sys
from part_finder.forms_search import RequirementForm
from part_finder.forms_user import *
from part_finder.views_search import *
# from part_finder.views import index
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist


# all views associated with participant and researcher

@login_required
# Check if user profile exists
def no_user_profile(request):
    return request.user.profile.researcher is None and request.user.profile.participant is None


# redirect to registration view
def redirect_to_reg(request):
    if request.user.profile.typex == 'Researcher':
        return redirect("/part_finder/researcher_registration/")
    if request.user.profile.typex == 'Participant':
        return redirect("/part_finder/participant_registration_1/")


# Check registration status once logged in
# if registration hasn't been completed, redirect to reg page
@login_required
def login_success(request):
    if no_user_profile(request):
        return redirect_to_reg(request)
    else:
        return redirect("index")


# participant registration
# after account signup, participant is redirected here to complete their participant profile
def participant_registration_1(request):
    if request.user.profile.participant is None:
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

    participant = request.user.profile.participant
    if not participant.reg_2_completed:
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


# Participant views
@login_required
# profile page
def profile_page(request):

    if no_user_profile(request):
        return redirect_to_reg(request)
    else:
        participant = request.user.profile.participant
        lang = participant.language.all()
        user = request.user

        context_dict = {'participant': participant, 'lang': lang, 'user': user}

    return render(request, 'part_finder/participant_profile.html', context_dict)


# Participant general details update
class UserAccountUpdate(UpdateView):

    model = User
    form_class = UserAccountUpdateForm
    template_name = 'part_finder/participant_update_form.html'
    success_url = '/part_finder/participant/profile'

    def get_object(self, queryset=None):
        return self.request.user.profile.participant


# Participant general details update
class ParticipantGeneralUpdate(UpdateView):

    model = Participant
    form_class = PartGeneralUpdateForm
    template_name = 'part_finder/participant_update_form.html'
    success_url = '/part_finder/participant/profile'

    def get_object(self, queryset=None):
        return self.request.user.profile.participant


# Participant student details update
class ParticipantStudentUpdate(UpdateView):

    model = Participant
    form_class = PartStudentUpdateForm
    template_name = 'part_finder/participant_update_form.html'
    success_url = '/part_finder/participant/profile'

    def get_object(self, queryset=None):
        return self.request.user.profile.participant


# Participant demo details update
class ParticipantDemoUpdate(UpdateView):

    model = Participant
    form_class = PartDemoUpdateForm
    template_name = 'part_finder/participant_update_form.html'
    success_url = '/part_finder/participant/profile'

    def get_object(self, queryset=None):
        return self.request.user.profile.participant


# Participant preferences details update
class ParticipantPrefUpdate(UpdateView):

    model = Participant
    form_class = PartPrefUpdateForm
    template_name = 'part_finder/participant_update_form.html'
    success_url = '/part_finder/participant/settings'

    def get_object(self, queryset=None):
        return self.request.user.profile.participant


# Participant preferences details update (non-student)
# prevents non students from being able to update the "My Uni Only" preference.
class ParticipantPrefUpdateNS(UpdateView):

    model = Participant
    form_class = PartPrefUpdateFormNS
    template_name = 'part_finder/participant_update_form.html'
    success_url = '/part_finder/participant/settings'

    def get_object(self, queryset=None):
        return self.request.user.profile.participant


@login_required
# user settings page
def settings_page(request):
    participant = request.user.profile.participant

    context_dict = {'participant': participant, }

    return render (request, 'part_finder/settings.html', context_dict)


# refresh requirements after an update has been made.
def refresh_reqs(experiment):

    try:
        requirement = Requirement.objects.get(experiment=experiment)

        # check requirements to see what reqs
        # the participant needs to have.
        if (requirement.age or requirement.language or requirement.height or
            requirement.gender or requirement.weight or requirement.student):
            requirement.match = True
            requirement.save()

        # If the requirements have been removed, set "match" back to false.
        if (requirement.age == False and requirement.language == False and requirement.height == False and
            requirement.weight == False and requirement.gender == False and requirement.student == False):
            requirement.match = False
            requirement.save()

        # Update timeslots
        timeslots = TimeSlot.objects.filter(experiment=experiment)
        for time_slot in timeslots:
            time_slot.end_time = str(datetime.timedelta(hours=time_slot.start_time.hour, minutes=time_slot.start_time.minute) + datetime.timedelta(minutes=experiment.duration))[-8:]
            time_slot.save()

        # Check if req details object exists, if it doesn't exist, create one
        if requirement.match:
            MatchingDetail.objects.get_or_create(requirement=requirement)
    except ObjectDoesNotExist:
        pass


# Displays list of experiments belonging to a researcher
@login_required
def researcher_experiments(request):

    experiments = Experiment.objects.filter(researcher=request.user.profile.researcher)

    # refresh_reqs for all experiments
    for e in experiments:
        refresh_reqs(e)

    requirements = Requirement.objects.all()
    match_details = MatchingDetail.objects.all()

    # count the number of experiments that have not ended
    exp_count = len([e for e in experiments if not e.has_ended])

    payment = Payment.objects.all()

    context_dict = {'experiments': experiments, 'exp_count': exp_count, 'payment': payment,
                    'requirements': requirements, 'match_details': match_details}

    return render(request, 'part_finder/myexperiments.html', context_dict)


# Display participant experiment applications
@login_required
def participant_experiments(request):

    if request.user.profile.typex != 'Participant':
        return HttpResponseRedirect(reverse('index'))
    else:
        applications = Application.objects.filter(participant=request.user.profile.participant)

        con_count = len([a for a in applications if a.status == 'Accepted' and not a.experiment.has_ended])
        pen_count = len([a for a in applications if a.status == 'Pending' and not a.experiment.has_ended])

        context_dict = {'applications': applications, 'con_count': con_count, 'pen_count': pen_count}

        return render(request, 'part_finder/participant_experiments.html', context_dict)


# Displays list of ended experiments belonging to a researcher
@login_required
def participant_experiment_history(request):

    context_dict = {'applications': Application.objects.filter(participant=request.user.profile.participant)}
    return render(request, 'part_finder/participant_experiment_history.html', context_dict)


# Researcher profile page
def researcher_profile(request, username):
    user = User.objects.get(username=username)
    user_profile = UserProfile.objects.get(user=user)
    researcher = user_profile.researcher
    experiments = Experiment.objects.filter(researcher=researcher)

    context_dict = {'researcher': researcher, 'experiments': experiments}

    return render(request, 'part_finder/researcher_profile.html/', context_dict)


# Researcher details update
class ResearcherUpdate(UpdateView):
    model = Researcher
    form_class = ResearcherForm
    template_name_suffix = '_update_form'
    success_url='/part_finder/researcher/update'

    def get_object(self, queryset=None):
        return self.request.user.profile.researcher


# Researcher registration form
@login_required
def researcher_registration(request):
    if request.user.profile.researcher is None:
        if request.method == 'POST':
            researcher_form = ResearcherForm(request.POST)
            if request.user.profile.typex == 'Researcher' and researcher_form.is_valid():
                res = researcher_form.save()
                profile = request.user.profile
                profile.researcher = res
                profile.save()
                return HttpResponseRedirect(reverse('index'))
            else:
                print researcher_form.errors
        else:
            researcher_form = ResearcherForm()
    else:
        return redirect("index")
    return render(request, 'part_finder/researcher_registration.html', {'researcher_form': researcher_form})
