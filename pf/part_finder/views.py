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
from django.views.generic.list import ListView
from django.forms.formsets import formset_factory, BaseFormSet
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
import sys
from part_finder.forms_search import RequirementForm
from part_finder.views_search import *
from part_finder.forms_user import ResearcherForm, SignupForm
# from part_finder.views_user import no_user_profile
import views_user
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django import template
from django.core.mail import send_mail
from pf.settings import SITE_ADDRESS
from part_finder.emails import *

# register = template.Library()
from django.template import RequestContext # For CSRF
# Create your views here.



#Homepage
def index(request):
    experiments_list = Experiment.objects.all()[:10]
    payment_list = Payment.objects.all()
    request = request
    app = None
    filtered_exp = []

    # Display experiments based on user preferences
    for e in experiments_list:
        try:
            if request.user.is_authenticated() and request.user.profile.typex == 'Participant' and request.user.profile.participant != None :
                if participant_pref_filter(request, e) == 0:
                    filtered_exp.append(e)
            else:
                filtered_exp = experiments_list
        except AttributeError:
            pass

    context_dict = {'experiments' : experiments_list, 'payment_list': payment_list, 'request': request, 'filtered_exp':filtered_exp, 'app': app}
    return render(request, 'part_finder/index.html', context_dict)



#Experiment timeslots
@login_required
def exp_timeslots(request, experiment_id):
    researcher = request.user.profile.researcher
    experiment = Experiment.objects.get(id=experiment_id, researcher=researcher)
    timeslots = TimeSlot.objects.filter(experiment=experiment)

    context_dict = {'experiment': experiment, 'timeslots': timeslots}

    return render(request, 'part_finder/timeslots.html', context_dict)



#Displays list of ended experiments belonging to a researcher
@login_required
def experiment_history(request):
    experiments = Experiment.objects.filter(researcher=request.user.profile.researcher)

    context_dict = {'experiments': experiments}

    return render(request, 'part_finder/experiment_history.html', context_dict)


# Application Counter - Count number of applications for an experiment
def application_counter(exp):

    applications = Application.objects.filter(experiment=exp)

    #increment the current parts counter
    for app in applications:

        #increment if status is updated to accepted
        if app.status == 'Accepted':
            app.timeslot.current_parts += 1
            app.timeslot.save()
            print sys.stdout.write('Increment')

        #check to see if experiments are full
        if app.timeslot.current_parts >= app.timeslot.no_of_parts:
            app.timeslot.is_full = True
            app.timeslot.save()
        elif app.timeslot.current_parts <= app.timeslot.no_of_parts:
            app.timeslot.is_full = False
            app.timeslot.save()


# Displays page for researcher to process experiment applications
@login_required
def process_application(request, experiment_name_slug, r_slug):
    experiment = Experiment.objects.get(slug=experiment_name_slug, researcher_slug=r_slug)
    application = Application.objects.filter(researcher=request.user.profile.researcher, experiment=experiment)
    timeslots = TimeSlot.objects.filter(experiment=experiment).order_by('date')

    context_dict = {'app': application, 'time': timeslots, 'experiment': experiment}

    return render(request, 'part_finder/process_applications.html', context_dict )


# Displays page to update application status
@login_required
def update_application_status(request, exp_id, app_id):
    context_dict = {}

    researcher = request.user.profile.researcher
    experiment = Experiment.objects.get(id=exp_id)
    application = Application.objects.get(researcher=researcher, experiment=experiment, id=app_id)
    timeslot = TimeSlot.objects.get(application=application)

    if request.method == 'POST':
        #if timeslot is full, dont allow applicant to be marked as accepted
        def get_app_form_post():
            if application.timeslot.is_full == True:
                return UpdateStatusFormFull(request.POST)
            else:
                return UpdateStatusForm(request.POST)

        temp_app_form = get_app_form_post()

        if temp_app_form.is_valid():
            temp_app = temp_app_form.save(commit=False)
            application.status = temp_app.status
            application.save()
            #set counter to zero
            application.timeslot.current_parts = 0
            application.timeslot.save()
            application_counter(experiment)

            #emails
            app_status_update_email(application)

            return process_application(request, experiment.slug, experiment.researcher_slug)

        else:
            print temp_app_form.errors
    else:
        def get_app_form():
            if application.timeslot.is_full == True:
                return UpdateStatusFormFull()
            else:
                return UpdateStatusForm()

        temp_app_form = get_app_form()

    context_dict = {'update_form': temp_app_form, 'researcher': researcher, 'experiment': experiment, 'application':application}

    return render(request, 'part_finder/process_application_status.html', context_dict)



#Check if all timeslots for an experiment are full
def experiment_full(experiment):
    timeslots = TimeSlot.objects.filter(experiment=experiment)
    counter =0
    ts = 0

    for timeslot in timeslots:
        counter+= 1
        ts += timeslot.is_full

    if ts == counter:
        experiment.is_full = True
        experiment.save()
    else:
        experiment.is_full = False
        experiment.save()



# Display all experiments
def all_experiments(request):
    experiments = Experiment.objects.all()
    payment_list = Payment.objects.all()
    request = request

    filtered_exp = []

    try:
        for e in experiments:
            if request.user.is_authenticated() and request.user.profile.typex == 'Participant' and request.user.profile.participant != None:
                if participant_pref_filter(request, e) == 0:
                    filtered_exp.append(e)
            else:
                filtered_exp = experiments
    except AttributeError:
        pass

    context_dict = {'experiments': experiments, 'payment_list': payment_list, 'request': request, 'filtered_exp':filtered_exp}

    return render (request, 'part_finder/all_experiments.html', context_dict)


# Get requirements for an experiment
def get_requirements(experiment):
    reqs = Requirement.objects.get(experiment=experiment)

    for attr, value in reqs.__dict__.iteritems.filter(id):
        if attr == 'id' or attr == 'match' or attr == 'experiment_id' or attr == '_state':
           pass
        else:
            print attr, value


# Display single experiment
def experiment (request, experiment_name_slug, r_slug):
    context_dict = {}
    try:
        experiment = Experiment.objects.get(slug=experiment_name_slug, researcher_slug=r_slug)
        experiment_list = Experiment.objects.filter(slug=experiment_name_slug)
        appform = ApplicationForm(experiment)
        timeslots = TimeSlot.objects.filter(experiment=experiment).order_by("date")
        researcher = experiment.researcher
        payment = Payment.objects.get(experiment=experiment)
        valid = ''
        part_valid = ''


        #check if all experiment timeslots are full
        experiment_full(experiment)

        # get user applications
        def get_user_apps():
            if request.user.is_anonymous():
                a = Application.objects.all()
                return a
            else:
                a = Application.objects.filter(participant=request.user.profile.participant)
                return a

        a = get_user_apps()

        #check if user has already applied for experiment
        def check_already_applied():
            applied = False

            for Application in a:
                if Application.experiment.id == experiment.id:
                    applied = True

            return applied

        userapplied = check_already_applied()

        #get participant requirment details
        try:
            reqs = Requirement.objects.get(experiment=experiment)
            match_detail = MatchingDetail.objects.get(requirement=reqs)
            # Remove special characters from language_req string
            language_req = match_detail.l.replace('[','').replace('u','').replace("'",'').replace(']','')

        except (Requirement.DoesNotExist, MatchingDetail.DoesNotExist) , e:
            reqs = None
            match_detail = None
            language_req = None


        if views_user.no_user_profile(request) == True:
            pass
            # return redirect_to_reg(request)
        else:

            try:
            #Check if logged in participant meets requirements.
                if request.user.is_authenticated() and request.user.profile.typex == 'Participant':
                    check_eligible_valid = check_applicant_validity(request, experiment)

                    if check_eligible_valid == 0:
                        valid = True
                    else:
                        valid = False

                    #check against participant preferences
                    check_part_pref_valid = participant_pref_filter(request, experiment)


                    if check_part_pref_valid == 0:
                        part_valid = True
                    else:
                        part_valid = False

            except (MatchingDetail.DoesNotExist , Requirement.DoesNotExist , reqs.DoesNotExist) , e:
                reqs = None
                match_detail = None


        # check if eparticipant preferences


        context_dict= {'appform': appform, 'experiment_name': experiment.name, 'single_experiment': experiment_list,
                       'experiment': experiment, 'user_applied': userapplied, 'timeslots': timeslots, 'researcher': researcher, 'payment': payment, 'valid': valid,
                       'reqs': reqs, 'match_detail': match_detail, 'lang_req': language_req, 'part_valid': part_valid }


        # process experiment application form
        if request.method == 'POST':

             appform = ApplicationForm(experiment, request.POST)

             if appform.is_valid():
                application = appform.save(commit=False)
                application.researcher = experiment.researcher
                application.participant = request.user.profile.participant
                application.experiment = experiment
                application.status = 'Pending'
                application.save()
                experiment_app_email(application)

                return HttpResponseRedirect(reverse('participant_experiments'))

             else:
                print appform.errors

    except (Experiment.DoesNotExist , Payment.DoesNotExist) , p:
        payment = None

    return render(request, 'part_finder/experiments.html', context_dict )



# Add experiment
@login_required
def add_experiment(request):

    class RequiredFormSet(BaseFormSet):
        def __init__(self, *args, **kwargs):
            super(RequiredFormSet, self).__init__(*args, **kwargs)
            for form in self.forms:
                form.empty_permitted = False

    TimeSlotFormSet = formset_factory(TimeSlotForm, max_num=10, formset=RequiredFormSet)

    if request.method == 'POST':
        form = ExperimentForm(request.POST)

        payment_form = PaymentForm(request.POST)
        requirement_form = RequirementForm(request.POST)
        # Create a formset from the submitted data
        time_slot_formset = TimeSlotFormSet(request.POST, request.FILES)
        if form.is_valid() and time_slot_formset.is_valid() and payment_form.is_valid() and requirement_form.is_valid():
            experiment = form.save(commit=False)
            res = request.user.profile.researcher
            experiment.researcher = res
            form.save()

            #payment form details
            payment = payment_form.save(commit=False)
            payment.experiment = experiment
            payment_form.save()

            #requirement form details
            requirement = requirement_form.save(commit=False)
            requirement.experiment = experiment
            # requirement_form.save()

            #check experiment to see if it is matched and
            #set matched bool to true.


            # # set matched experiment to true
            if requirement.age == '1':
                requirement.match = True
            if requirement.language == '1':
                requirement.match = True
            if requirement.height == '1':
                requirement.match = True
            if requirement.weight == '1':
                requirement.match = True
            if requirement.gender == '1':
                requirement.match = True
            if requirement.student == '1':
                requirement.match = True

            requirement_form.save()

            for form in time_slot_formset.forms:
                time_slot = form.save(commit=False)
                # todo_item.list = todo_list
                time_slot.experiment = experiment
                time_slot.save()

            # if only student is true then redirect to res exp area
            if (requirement.age == '0' and requirement.language == '0' and requirement.height == '0' and requirement.weight == '0' and requirement.gender == '0' and requirement.student == '1'):
                return HttpResponseRedirect(reverse('researcher_experiments'))
            elif requirement.match == True:
                return HttpResponseRedirect(reverse('set_match', args=[experiment.id] ))
            else:
                return HttpResponseRedirect(reverse('researcher_experiments'))

        else:
            print form.errors
            print requirement_form.errors
            print payment_form.errors

    else:
        form = ExperimentForm()

        time_slot_formset = TimeSlotFormSet()
        payment_form = PaymentForm()
        requirement_form = RequirementForm()

    c = {'form':form, 'time_slot_formset': time_slot_formset, 'payment_form': payment_form, 'requirement_form': requirement_form}
    c.update(csrf(request))

    return render(request, 'part_finder/add_experiment.html', c)




# Update experiment
class ExperimentUpdate(UpdateView):
    model = Experiment
    form_class = ExperimentForm
    template_name = 'part_finder/experiment_update.html'
    success_url='/part_finder/current_experiments/'


    def get_queryset(self):
        qs = super(ExperimentUpdate, self).get_queryset()
        exp = qs.filter(researcher=self.request.user.profile.researcher)
        return exp



#Update experiment payment info.
class PaymentUpdate(UpdateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'part_finder/experiment_update.html'
    success_url='/part_finder/current_experiments/'

    def get_queryset(self):
        qs = super(PaymentUpdate, self).get_queryset()
        exp = Experiment.objects.get(id=self.kwargs['slug'])
        return qs.filter(experiment=exp)



#Update experiment timeslot
class TimeSlotUpdate(UpdateView):
    model = TimeSlot
    form_class = TimeSlotForm
    template_name = 'part_finder/experiment_update.html'
    success_url='/part_finder/current_experiments/'


    def get_queryset(self):
        qs = super(TimeSlotUpdate, self).get_queryset()
        exp = Experiment.objects.get(id=self.kwargs['slug'])
        return qs.filter(experiment=exp)


# Update experiment requirements
class RequirementUpdate(UpdateView):
    model = Requirement
    form_class = RequirementForm
    template_name = 'part_finder/experiment_update.html'
    success_url='/part_finder/current_experiments/'


    def get_queryset(self):
        qs = super(RequirementUpdate, self).get_queryset()
        exp = Experiment.objects.get(id=self.kwargs['slug'])
        return qs.filter(experiment=exp)


# Update experiment requirement details
class MatchDetailsUpdate(UpdateView):

    model = MatchingDetail
    form_class = MatchingDetailForm
    template_name = 'part_finder/experiment_update.html'
    success_url='/part_finder/current_experiments/'


    def get_queryset(self):
        qs = super(MatchDetailsUpdate, self).get_queryset()
        req = Requirement.objects.get(id=self.kwargs['slug'])
        return qs.filter(requirement=req)



@login_required
#Delete experiment
def delete_experiment(request, experiment_id):
    r = request.user.profile.researcher
    e = Experiment.objects.get(id=experiment_id, researcher=r)


    if request.method == 'POST':
        e.delete()
        return HttpResponseRedirect("/part_finder/current_experiments/")

    context_dict = {'experiment': e}
    return render(request, 'part_finder/delete_experiment.html', context_dict)



@login_required
#Delete participant experiment
def delete_participant_experiment(request, experiment_id):
    p = request.user.profile.participant

    e = Experiment.objects.get(id=experiment_id)
    a = Application.objects.get(experiment=e, participant=p)

    if request.method == 'POST':
        a.delete()
        return HttpResponseRedirect("/part_finder/my_experiments/")

    context_dict = {'experiment': e}
    return render(request, 'part_finder/delete_participant_experiment.html', context_dict)



@login_required
#Mark experiment as ended
def end_experiment(request, experiment_id):
    r = request.user.profile.researcher
    e = Experiment.objects.get(id=experiment_id, researcher=r)


    if request.method == 'POST':
        e.has_ended = True
        e.save()
        return HttpResponseRedirect("/part_finder/current_experiments/")

    context_dict = {'experiment': e}

    return render(request, 'part_finder/end_experiment.html', context_dict)


@login_required
#Reactivate experiment as ended
def reac_experiment(request, experiment_id):
    r = request.user.profile.researcher
    e = Experiment.objects.get(id=experiment_id, researcher=r)


    if request.method == 'POST':
        e.has_ended = False
        e.save()
        return HttpResponseRedirect("/part_finder/experiment_history/")

    context_dict = {'experiment': e}

    return render(request, 'part_finder/reactivate_experiment.html', context_dict)



