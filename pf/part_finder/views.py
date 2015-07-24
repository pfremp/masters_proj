from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, request
from part_finder.models import Researcher, Experiment, Participant, UserProfile, Contact, User,Dummy, Payment
from part_finder.forms import ExperimentForm, ResearcherForm, PartDetailsForm, ParticipantForm, SignupForm, TodoList, TimeSlotForm, TimeSlotFrom, PaymentForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# from django.contrib.formtools.wizard.views import SessionWizardView
from formtools.wizard.views import WizardView, SessionWizardView
from django.views.generic.edit import UpdateView

from django.forms.formsets import formset_factory, BaseFormSet
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext # For CSRF
# Create your views here.

#Homepage
def index(request):
    experiments_list = Experiment.objects.all()[:10]
    # experiments_list = Experiment.objects.order_by('date')[:10]
    context_dict = {'experiments' : experiments_list}
    return render(request, 'part_finder/index.html', context_dict)



#Check if user profile exists
def no_user_profile(request):
    if request.user.profile.researcher == None and request.user.profile.participant == None:
        return True
    else:
        return False
    # try:
    #     if request.user.profile.researcher == None and request.user.profile.participant == None:
    #         return True
    #     # else: return False
    # except UserProfile.DoesNotExist:
    #     return True


#Check registration status once logged in
#if registration hasnt been completed, redirect to reg page
@login_required
def login_success(request):
    if no_user_profile(request) == True:
        if request.user.profile.typex == 'Researcher':
            return redirect("/part_finder/researcher_registration/")
        if request.user.profile.typex == 'Participant':
            return redirect("/part_finder/participant_registration/")
    else:
        return redirect("index")



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



#participant wizard form conditional check
def show_message_form_condition(wizard):
    # try to get the cleaned data of step 1
    cleaned_data = wizard.get_cleaned_data_for_step('0') or {}
    # check if the field ``leave_message`` was checked.
    return cleaned_data.get('student', True)




# Particiapnt Registration form
# Multi-page form using django form wizard
class ParticipantRegistration(SessionWizardView):
    template_name = "part_finder/participant_registration.html"
    def done(self, form_list, **kwargs):
        request = self.request
        form_data = process_form_data(form_list, request)
        return render_to_response('part_finder/update_profile.html', {'form_data': form_data })


#Process multi page form data and save to Participant Object
# http://stackoverflow.com/questions/5769347/easiest-way-to-save-django%C2%B4s-formwizard-form-list-in-db
def process_form_data(form_list, request):
    form_data = [form.cleaned_data for form in form_list]
    instance = Participant()
    for form in form_list:
        for field, value in form.cleaned_data.iteritems():
            setattr(instance, field, value)
    instance.save()
    #Assign participant to UserProfile
    profile = request.user.profile
    profile.participant = instance
    profile.save()

    return form_data


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
def experiment (request, experiment_name_slug, r_slug):

    context_dict = {}
    try:
        experiment = Experiment.objects.get(slug=experiment_name_slug, researcher_slug=r_slug)
        context_dict['experiment_name'] = experiment.name
        experiment_list = Experiment.objects.filter(slug=experiment_name_slug)
        context_dict['single_experiment'] = experiment_list
        context_dict['experiment'] = experiment
    except Experiment.DoesNotExist:
        pass
    return render(request, 'part_finder/experiments.html', context_dict)

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
        # Create a formset from the submitted data
        time_slot_formset = TimeSlotFormSet(request.POST, request.FILES)
        if form.is_valid() and time_slot_formset.is_valid() and payment_form.is_valid():
            experiment = form.save(commit=False)
            res = request.user.profile.researcher
            experiment.researcher = res
            form.save()

            #payment form details
            payment = payment_form.save(commit=False)
            payment.experiment = experiment
            payment_form.save()

            for form in time_slot_formset.forms:
                time_slot = form.save(commit=False)
                # todo_item.list = todo_list
                time_slot.experiment = experiment
                time_slot.save()



        # if todo_list_form.is_valid() and todo_item_formset.is_valid():
        #     todo_list = todo_list_form.save()
        #     for form in todo_item_formset.forms:
        #         todo_item = form.save(commit=False)
        #         # todo_item.list = todo_list
        #         todo_item.experiment = experiment
        #         todo_item.save()


            return index(request)
        else:
            print form.errors
    else:
        form = ExperimentForm()
        ##time_slot_form = TimeSlotFrom()
        time_slot_formset = TimeSlotFormSet()
        payment_form = PaymentForm()

    # For CSRF protection
    # See http://docs.djangoproject.com/en/dev/ref/contrib/csrf/
    c = {'form':form,'time_slot_formset': time_slot_formset, 'payment_form': payment_form}
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





#Researcher details update
class ResearcherUpdate(UpdateView):
    model = Researcher
    form_class = ResearcherForm
    fields = ['dob', 'matric', 'institution', 'contact_no', 'department']
    template_name_suffix = '_update_form'
    success_url='/part_finder/participant/update'

    def get_object(self, queryset=None):
        return self.request.user.profile.researcher

    # def get_object(self):
    #     return get_object_or_404(User, pk=request.session['user_id'])

    # def get_object(self, request):
    #     return get_object_or_404(Participant, pk=request.session['user_id'])


    # def get_object(self, queryset=None):
    #     return self.request.user

    # def get_object(self):
    #     return self.request.user.get_profile()

    # def get_object(self):
    #     return Participant.objects.get(pk=self.request.GET.get('pk'))
    #     # return Participant.objects.get(user=self.request.GET.get('user'))
    #     # return Participant.objects.get(Participant.userprofile.user=self.request.user)
    # def get_object(self):
    #     return Participant.objects.get(Participant.userprofile.user=self.request.user)
        # return Participant.objects.get(id=self.request.id)




# def update_location(request, pk=None):
#     obj = get_object_or_404(Participant, pk=pk)
#     form = LocationForm(request.POST or None,
#                         request.FILES or None, instance=obj)
#     if request.method == 'POST':
#         if form.is_valid():
#            form.save()
#            return redirect('/accounts/loggedin/locations/all/')
#     return render(request, 'locations/location_update.html', {'form': form})
#



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


