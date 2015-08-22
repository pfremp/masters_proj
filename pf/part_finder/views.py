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
from django.views.generic.list import ListView
from django.forms.formsets import formset_factory, BaseFormSet
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
import sys
from part_finder.forms_search import RequirementForm
from part_finder.views_search import *
# from part_finder.views_user import no_user_profile
import views_user
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django import template

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

    for e in experiments_list:
        # print "experiment " + str(e)
        # print "Test " + str(participant_pref_filter(request, e))
        try:
            if request.user.is_authenticated() and request.user.profile.typex == 'Participant' and request.user.profile.participant != None :
                if participant_pref_filter(request, e) == 0:
                    filtered_exp.append(e)

                    # for x in request.user.profile.participant.experiments.all():
                    #     if x == e:
                    #         app = False
                    #     else:
                    #         app = True

            else:
                filtered_exp = experiments_list


        except AttributeError:
            pass





    context_dict = {'experiments' : experiments_list, 'payment_list': payment_list, 'request': request, 'filtered_exp':filtered_exp, 'app': app}
    return render(request, 'part_finder/index.html', context_dict)

# def current_user(request):
#
#
#
#     user = request.user.profile.participant.application

# @login_required
# #Check if user profile exists
# def no_user_profile(request):
#     if request.user.profile.researcher == None and request.user.profile.participant == None:
#         return True
#     else:
#         return False
#     # try:
#     #     if request.user.profile.researcher == None and request.user.profile.participant == None:
#     #         return True
#     #     # else: return False
#     # except UserProfile.DoesNotExist:
#     #     return True
#
#
# #Check registration status once logged in
# #if registration hasnt been completed, redirect to reg page
# @login_required
# def login_success(request):
#     if no_user_profile(request) == True:
#         if request.user.profile.typex == 'Researcher':
#             return redirect("/part_finder/researcher_registration/")
#         if request.user.profile.typex == 'Participant':
#             return redirect("/part_finder/participant_registration_1/")
#     else:
#         return redirect("index")






#refresh requirements after an update has been made.
def refresh_reqs(experiment):

    requirement = Requirement.objects.get(experiment=experiment)

    #check requirements to see what reqs
    #  the participant needs to have.
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

    requirement.save()

    #If the requirements have been removed, set "match" back to false.
    if requirement.age != '1' and requirement.language != '1' and requirement.height != '1' and requirement.weight != '1' and requirement.gender != '1' and requirement.student != '1':
        requirement.match = False
        requirement.save()



    #Check if req details object exists, if it doesn't exist, create one
    if requirement.match == True:
        match_details = MatchingDetail.objects.get_or_create(requirement=requirement)





#test masonary
def masonary(request):

    return render (request, 'part_finder/bootstrap-masonry-template.htm')


#Researcher registration form
@login_required
def researcher_registration(request):
    if request.user.profile.researcher == None:
        if request.method == 'POST':
            researcher_form = ResearcherForm(request.POST)
            if request.user.profile.typex == 'Researcher':
                if researcher_form.is_valid():
                    res = researcher_form.save()
                    profile = request.user.profile
                    profile.researcher = res
                    profile.save()
                    return index(request)
                else:
                    print researcher_form.errors
        else:
            researcher_form = ResearcherForm()
    else:
        return redirect("index")
    return render(request, 'part_finder/researcher_registration.html', {'researcher_form': researcher_form})

#
#
# #participant wizard form conditional check
# def show_message_form_condition(wizard):
#     # try to get the cleaned data of step 1
#     cleaned_data = wizard.get_cleaned_data_for_step('0') or {}
#     # check if the field ``leave_message`` was checked.
#     return cleaned_data.get('student', True)
#
#
#
#
# # Particiapnt Registration form
# # Multi-page form using django form wizard
# class ParticipantRegistration(SessionWizardView):
#     template_name = "part_finder/participant_registration.html"
#     def done(self, form_list, **kwargs):
#         request = self.request
#         form_data = process_form_data(form_list, request)
#         return render_to_response('part_finder/update_profile.html', {'form_data': form_data })
#
#
# #Process multi page form data and save to Participant Object
# # http://stackoverflow.com/questions/5769347/easiest-way-to-save-django%C2%B4s-formwizard-form-list-in-db
# def process_form_data(form_list, request):
#     form_data = [form.cleaned_data for form in form_list]
#     instance = Participant()
#     for form in form_list:
#         for field, value in form.cleaned_data.iteritems():
#             setattr(instance, field, value)
#     instance.save()
#     #Assign participant to UserProfile
#     profile = request.user.profile
#     profile.participant = instance
#     profile.save()
#
#     return form_data

# def
#
# #experiment page
# def experiment (request, experiment_name_slug):
#
#     context_dict = {}
#     try:
#         experiment = Experiment.objects.get(slug=experiment_name_slug)
#         context_dict['experiment_name'] = experiment.name
#         experiment_list = Experiment.objects.filter(slug=experiment_name_slug)
#         context_dict['single_experiment'] = experiment_list
#         context_dict['experiment'] = experiment
#     except Experiment.DoesNotExist:
#         pass
#     return render(request, 'part_finder/experiments.html', context_dict)

    #experiment page

#Displays list of experiments belonging to a researcher
@login_required
def researcher_experiments(request):
    context_dict = {}


    # experiments = Experiment.objects.filter(researcher=request.user.profile.researcher)
    experiments = Experiment.objects.filter(researcher=request.user.profile.researcher)

    #refresh_reqs for all experiments
    for e in experiments:
        refresh_reqs(e)

    requirements = Requirement.objects.all()
    match_details = MatchingDetail.objects.all()


    def get_exp_count():
        count = 0
        for e in experiments:
            if e.has_ended == False:
                count += 1
        return count

    exp_count = get_exp_count()

    payment = Payment.objects.all()

    context_dict = {'experiments': experiments, 'exp_count': exp_count, 'payment': payment, 'requirements': requirements, 'match_details': match_details}

    return render(request, 'part_finder/myexperiments.html', context_dict)

#timeslots
@login_required
def exp_timeslots(request, experiment_id):
    researcher = request.user.profile.researcher
    experiment = Experiment.objects.get(id=experiment_id, researcher=researcher)
    timeslots = TimeSlot.objects.filter(experiment=experiment)


    context_dict = {'experiment': experiment, 'timeslots': timeslots}


    return render(request, 'part_finder/timeslots.html', context_dict)



@login_required
def participant_experiments(request):
    context_dict = {}

    if request.user.profile.typex != 'Participant':
        return HttpResponseRedirect("/part_finder/")
    else:

        applications = Application.objects.filter(participant=request.user.profile.participant)


        def get_confirmed_experiments():
            count = 0
            for a in applications:
                if a.status == 'Accepted' and a.experiment.has_ended == False:
                    count += 1
            return  count

        def get_pen_experiments():
            count = 0
            for a in applications:
                if a.status == 'Pending' and a.experiment.has_ended == False:
                    count += 1
            return  count

        con_count = get_confirmed_experiments()
        pen_count = get_pen_experiments()



        context_dict = {'applications': applications, 'con_count': con_count, 'pen_count': pen_count}

        return render(request, 'part_finder/participant_experiments.html', context_dict)

#Displays list of ended experiments belonging to a researcher
@login_required
def experiment_history(request):
    context_dict = {}

    # experiments = Experiment.objects.filter(researcher=request.user.profile.researcher)
    experiments = Experiment.objects.filter(researcher=request.user.profile.researcher)


    context_dict = {'experiments': experiments}

    return render(request, 'part_finder/experiment_history.html', context_dict)


#Displays list of ended experiments belonging to a researcher
@login_required
def participant_experiment_history(request):
    context_dict = {}
    p = request.user.profile.participant
    a = Application.objects.filter(participant=p)
    context_dict = {'applications': a}
    return render(request, 'part_finder/participant_experiment_history.html', context_dict)


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






@login_required
def process_application(request, experiment_name_slug, r_slug):
    context_dict = {}
    # experiment = Experiment.objects.filter(slug=experiment_name_slug, researcher_slug=r_slug)
    experiment = Experiment.objects.get(slug=experiment_name_slug, researcher_slug=r_slug)
    application = Application.objects.filter(researcher=request.user.profile.researcher, experiment=experiment)
    timeslots = TimeSlot.objects.filter(experiment=experiment).order_by('date')


    context_dict = {'app': application, 'time': timeslots, 'experiment': experiment}

    return render(request, 'part_finder/process_applications.html', context_dict )

@login_required
def update_application_status(request, exp_id, app_id):
    context_dict = {}

    researcher = request.user.profile.researcher
    experiment = Experiment.objects.get(id=exp_id)
    application = Application.objects.get(researcher=researcher, experiment=experiment, id=app_id)
    # timeslots = TimeSlot.objects.filter(application=application)
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


    #testing




    # # for app in application:
    # for timeslot in timeslots:
    #     if timeslot.application == application:
    #          # if app.status == 'Accepted':
    #         timeslot.current_parts = 20
    #         timeslot.save()


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

#view all expriments
def all_experiments(request):
    experiments = Experiment.objects.all()
    payment_list = Payment.objects.all()
    request = request


    filtered_exp = []

    try:
        for e in experiments:
            # print "experiment " + str(e)
            # print "Test " + str(participant_pref_filter(request, e))
            if request.user.is_authenticated() and request.user.profile.typex == 'Participant' and request.user.profile.participant != None:
                if participant_pref_filter(request, e) == 0:
                    filtered_exp.append(e)
            else:
                filtered_exp = experiments
    except AttributeError:
        pass

    context_dict = {'experiments': experiments, 'payment_list': payment_list, 'request': request, 'filtered_exp':filtered_exp}


    return render (request, 'part_finder/all_experiments.html', context_dict)



def get_requirements(experiment):

    reqs = Requirement.objects.get(experiment=experiment)

    for attr, value in reqs.__dict__.iteritems.filter(id):
        if attr == 'id' or attr == 'match' or attr == 'experiment_id' or attr == '_state':
           pass
        else:
            print attr, value






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
                # context_dict = {'apps': user_apps}
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
                return HttpResponseRedirect(reverse('participant_experiments'))

             else:
                print appform.errors

    except (Experiment.DoesNotExist , Payment.DoesNotExist) , p:
        payment = None



    return render(request, 'part_finder/experiments.html', context_dict )


#
# def application(request, experiment, timeslot):
#
#     context_dict = {}






# #add experiment form
# @login_required
# def add_experiment(request):
#     if request.method == 'POST':
#         form = ExperimentForm(request.POST)
#         if form.is_valid():
#             experiment = form.save(commit=False)
#             res = request.user.profile.researcher
#             experiment.researcher = res
#             form.save()
#             return index(request)
#         else:
#             print form.errors
#     else:
#         form = ExperimentForm()
#
#     return render(request, 'part_finder/add_experiment.html', {'form':form})
#

# @login_required
# def set_matched(requirement):
#
#     if requirement.age == '1':
#         requirement.match = True
#     if requirement.language == '1':
#         requirement.match = True
#     if requirement.height == '1':
#         requirement.match = True
#     if requirement.weight == '1':
#         requirement.match = True
#     if requirement.gender == '1':
#         requirement.match = True
#     if requirement.student == '1':
#         requirement.match = True
#
#     requirement_form.save()

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
        ##time_slot_form = TimeSlotFrom(request.POST) # A form bound to the POST data
        payment_form = PaymentForm(request.POST)
        requirement_form = RequirementForm(request.POST)
        # Create a formset from the submitted data
        time_slot_formset = TimeSlotFormSet(request.POST, request.FILES)
        if form.is_valid() and time_slot_formset.is_valid() and payment_form.is_valid() and requirement_form.is_valid():
        # if form.is_valid() and time_slot_formset.is_valid() and payment_form.is_valid():
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
            # set_matched(requirement)

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

            if requirement.match == True:
                return HttpResponseRedirect(reverse('set_match', args=[experiment.id] ))
            else:
                # empty_match_detail = models.MatchingDetail
                # empty_match_detail.requirement = requirement
                # empty_match_detail.save()
                return researcher_experiments(request)

        else:
            print form.errors
            print requirement_form.errors
            print payment_form.errors



        #old content
        # if todo_list_form.is_valid() and todo_item_formset.is_valid():
        #     todo_list = todo_list_form.save()
        #     for form in todo_item_formset.forms:
        #         todo_item = form.save(commit=False)
        #         # todo_item.list = todo_list
        #         todo_item.experiment = experiment
        #         todo_item.save()

            # if requirement.match == True:
            #     return matched_experiment(request)
            # else:
            # return researcher_experiments(request)

    else:
        form = ExperimentForm()
        ##time_slot_form = TimeSlotFrom()
        time_slot_formset = TimeSlotFormSet()
        payment_form = PaymentForm()
        requirement_form = RequirementForm()




    # For CSRF protection
    # See http://docs.djangoproject.com/en/dev/ref/contrib/csrf/
    # c = {'form':form,'time_slot_formset': time_slot_formset, 'payment_form': payment_form,}
    c = {'form':form, 'time_slot_formset': time_slot_formset, 'payment_form': payment_form, 'requirement_form': requirement_form}
    c.update(csrf(request))

    return render(request, 'part_finder/add_experiment.html', c)


# def index(request):
#     # This class is used to make empty formset forms required
#     # See http://stackoverflow.com/questions/2406537/django-formsets-make-first-required/4951032#4951032
#     class RequiredFormSet(BaseFormSet):
#         def __init__(self, *args, **kwargs):
#             super(RequiredFormSet, self).__init__(*args, **kwargs)
#             for form in self.forms:
#                 form.empty_permitted = False
#     TodoItemFormSet = formset_factory(TodoItemForm, max_num=10, formset=RequiredFormSet)
#     if request.method == 'POST': # If the form has been submitted...
#         todo_list_form = TodoListForm(request.POST) # A form bound to the POST data
#         # Create a formset from the submitted data
#         todo_item_formset = TodoItemFormSet(request.POST, request.FILES)
#
#         if todo_list_form.is_valid() and todo_item_formset.is_valid():
#             todo_list = todo_list_form.save()
#             for form in todo_item_formset.forms:
#                 todo_item = form.save(commit=False)
#                 todo_item.list = todo_list
#                 todo_item.save()
#             return HttpResponseRedirect('thanks') # Redirect to a 'success' page
#     else:
#         todo_list_form = TodoListForm()
#         todo_item_formset = TodoItemFormSet()
#
#     # For CSRF protection
#     # See http://docs.djangoproject.com/en/dev/ref/contrib/csrf/
#     c = {'todo_list_form': todo_list_form,
#          'todo_item_formset': todo_item_formset,
#         }
#     c.update(csrf(request))
#
#     return render_to_response('todo/index.html', c)


    # if request.method == 'POST': # If the form has been submitted...
    #     todo_list_form = TimeSlotFrom(request.POST) # A form bound to the POST data
    #     # Create a formset from the submitted data
    #     todo_item_formset = TodoItemFormSet(request.POST, request.FILES)
    #
    #     if todo_list_form.is_valid() and todo_item_formset.is_valid():
    #         todo_list = todo_list_form.save()
    #         for form in todo_item_formset.forms:
    #             todo_item = form.save(commit=False)
    #             todo_item.list = todo_list
    #             todo_item.save()
    #
    #         return HttpResponseRedirect('thanks') # Redirect to a 'success' page
    # else:
    #     todo_list_form = TimeSlotFrom()
    #     todo_item_formset = TodoItemFormSet()
    #
    # # For CSRF protection
    # # See http://docs.djangoproject.com/en/dev/ref/contrib/csrf/
    # c = {'todo_list_form': todo_list_form,
    #      'todo_item_formset': todo_item_formset,
    #     }
    # c.update(csrf(request))
    #
    # return render_to_response('todo.html', c)


# #dummy_form
# # @login_required
# def dummy(request):
#     if request.method == 'POST':
#         form = DummyForm(request.POST)
#         if form.is_valid():
#             dummy = form.save(commit=False)
#             # res = request.user.profile.researcher
#             # experiment.researcher = res
#             form.save()
#             return index(request)
#         else:
#             print form.errors
#     else:
#         form = DummyForm()
#
#     return render(request, 'part_finder/dummy.html', {'form':form})


#Participant details update
class ParticipantUpdate(UpdateView):

    model = Participant
    form_class = ParticipantForm
    # fields = ['address_line_1', 'address_line_2', 'city', 'postcode', 'contact_number', 'occupation', 'student','university', 'course_name', 'graduation_year', 'matric', 'gender' , 'ethnicity', 'religion', 'height', 'weight', 'max_distance', 'uni_only', 'online_only', 'paid_only']
    # fields = ['address_line_1', 'address_line_2', 'city', 'postcode', 'contact_number', 'occupation', 'student','university', 'course_name', 'graduation_year', 'matric', 'gender' , 'ethnicity', 'religion', 'height', 'weight', 'max_distance', 'uni_only', 'online_only', 'paid_only']
    template_name_suffix = '_update_form'
    success_url='/part_finder/participant/update'

    def get_object(self, queryset=None):
        return self.request.user.profile.participant





# #Profile update
# class ProfileUpdate(UpdateView):
#     model = UserProfile
#     form_class = SignupForm
#     fields = ['first_name', 'last_name', 'type', 'username', 'password1', 'password2']
#     template_name_suffix = '_update_form'
#     success_url='/part_finder/profile/update'
#
#     def get_object(self, queryset=None):
#         return self.request.user.profile


class ExperimentList(ListView):
    model = Experiment
    template_name = 'part_finder/experiment_list.html'

    def get_queryset(self):
        self.researcher = get_object_or_404(Researcher, id=self.args[0])
        return Experiment.objects.filter(researcher=self.researcher)




class ExperimentUpdate(UpdateView):

    model = Experiment
    form_class = ExperimentForm
    template_name = 'part_finder/experiment_update.html'
    success_url='/part_finder/current_experiments/'
    # fields = ['name','short_description','long_description','duration', 'city','address', 'url']

    def get_queryset(self):
        qs = super(ExperimentUpdate, self).get_queryset()
        exp = qs.filter(researcher=self.request.user.profile.researcher)
        return exp



class PaymentUpdate(UpdateView):

    model = Payment
    form_class = PaymentForm
    template_name = 'part_finder/experiment_update.html'
    success_url='/part_finder/current_experiments/'


    def get_queryset(self):
        qs = super(PaymentUpdate, self).get_queryset()
        exp = Experiment.objects.get(id=self.kwargs['slug'])
        return qs.filter(experiment=exp)



class TimeSlotUpdate(UpdateView):

    model = TimeSlot
    form_class = TimeSlotForm
    template_name = 'part_finder/experiment_update.html'
    success_url='/part_finder/current_experiments/'


    def get_queryset(self):
        qs = super(TimeSlotUpdate, self).get_queryset()
        exp = Experiment.objects.get(id=self.kwargs['slug'])
        return qs.filter(experiment=exp)


class RequirementUpdate(UpdateView):

    model = Requirement
    form_class = RequirementForm
    template_name = 'part_finder/experiment_update.html'
    success_url='/part_finder/current_experiments/'


    def get_queryset(self):
        qs = super(RequirementUpdate, self).get_queryset()
        exp = Experiment.objects.get(id=self.kwargs['slug'])
        return qs.filter(experiment=exp)


class MatchDetailsUpdate(UpdateView):

    model = MatchingDetail
    form_class = MatchingDetailForm
    template_name = 'part_finder/experiment_update.html'
    success_url='/part_finder/current_experiments/'


    def get_queryset(self):
        qs = super(MatchDetailsUpdate, self).get_queryset()
        req = Requirement.objects.get(id=self.kwargs['slug'])
        return qs.filter(requirement=req)




#Researcher details update
class ResearcherUpdate(UpdateView):
    model = Researcher
    form_class = ResearcherForm
    # fields = ['dob', 'matric', 'institution', 'contact_no', 'department']
    template_name_suffix = '_update_form'
    success_url='/part_finder/researcher/update'

    def get_object(self, queryset=None):
        return self.request.user.profile.researcher


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





#Researcher page
def researcher_profile(request, username):
    user = User.objects.get(username=username)
    user_profile = UserProfile.objects.get(user=user)
    researcher = user_profile.researcher
    experiments = Experiment.objects.filter(researcher=researcher)


    context_dict = {'researcher': researcher, 'experiments': experiments}

    return render(request, 'part_finder/researcher_profile.html/', context_dict)









#TEST TO DO FORM
def todo(request):
    # This class is used to make empty formset forms required
    # See http://stackoverflow.com/questions/2406537/django-formsets-make-first-required/4951032#4951032
    class RequiredFormSet(BaseFormSet):
        def __init__(self, *args, **kwargs):
            super(RequiredFormSet, self).__init__(*args, **kwargs)
            for form in self.forms:
                form.empty_permitted = False

    TodoItemFormSet = formset_factory(TimeSlotForm, max_num=10, formset=RequiredFormSet)

    if request.method == 'POST': # If the form has been submitted...
        todo_list_form = TimeSlotFrom(request.POST) # A form bound to the POST data
        # Create a formset from the submitted data
        todo_item_formset = TodoItemFormSet(request.POST, request.FILES)

        if todo_list_form.is_valid() and todo_item_formset.is_valid():
            todo_list = todo_list_form.save()
            for form in todo_item_formset.forms:
                todo_item = form.save(commit=False)
                todo_item.list = todo_list
                todo_item.save()

            return HttpResponseRedirect('thanks') # Redirect to a 'success' page
    else:
        todo_list_form = TimeSlotFrom()
        todo_item_formset = TodoItemFormSet()

    # For CSRF protection
    # See http://docs.djangoproject.com/en/dev/ref/contrib/csrf/
    c = {'todo_list_form': todo_list_form,
         'todo_item_formset': todo_item_formset,
        }
    c.update(csrf(request))

    return render_to_response('todo.html', c)


















# def login_page(request):
#
#     # experiments_list = Experiment.objects.order_by('date')[:10]
#     context_dict = {}
#
#
#
#     return render(request, 'login-page.html', context_dict)







#old complete reg

#
#
#  #old complete reg
# @login_required
# def complete_registration(request):
#
#
#     context_dict = {}
#
#
#
#     if request.user.profile.researcher == None and request.user.profile.participant == None:
#
#
#         if request.method == 'POST':
#             researcher_form = ResearcherForm(request.POST)
#             participant_form = ParticipantForm(request.POST)
#
#             if request.user.profile.typex == 'Researcher':
#
#                 if researcher_form.is_valid():
#                     res = researcher_form.save()
#                     profile = request.user.profile
#                     profile.researcher = res
#                     profile.save()
#
#                     return index(request)
#
#                 else:
#                     print researcher_form.errors
#
#             if request.user.profile.typex == 'Participant':
#
#                 if participant_form.is_valid():
#                     par = participant_form.save()
#                     profile = request.user.profile
#                     profile.participant = par
#                     profile.save()
#
#                     return index(request)
#
#                 else:
#                     print participant_form.errors
#
#
#         else:
#             researcher_form = ResearcherForm()
#             participant_form = ParticipantForm()
#
#     else:
#         return redirect("index")
#
#     return render(request, 'part_finder/complete_registration.html', {'researcher_form': researcher_form, 'participant_form': participant_form})
#














#
# #participant details form
# def participant_details(request):
#
#     if request.method == 'POST':
#         form = ParticipantForm(request.POST)
#
#         if form.is_valid():
#             form.save(commit=True)
#
#             return index(request)
#         else:
#             print form.errors
#
#     else:
#         form = ParticipantForm
#
#     return render(request, 'part_finder/participant_details.html', {'form':form})
#
#
# #Researcher signup
# def researcher_signup(request):
#     if request.method == 'POST':
#         researcherForm = ResearcherForm(request.POST)
#
#         if researcherForm.is_valid():
#             researcherForm.save(commit=True)
#
#             return index(request)
#         else:
#             print researcherForm.errors
#
#     else:
#         researcherForm = ResearcherForm()
#
#     return render(request, 'part_finder/researcher_signup.html', {'form': researcherForm})


