from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from part_finder.models import Researcher, Experiment, Participant, UserProfile, Contact
from part_finder.forms import ExperimentForm, ResearcherForm, ContactForm1,ContactForm2
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.formtools.wizard.views import SessionWizardView
# Create your views here.


def index(request):

    experiments_list = Experiment.objects.order_by('date')[:10]
    context_dict = {'experiments' : experiments_list}



    return render(request, 'part_finder/index.html', context_dict)



# def login_page(request):
#
#     # experiments_list = Experiment.objects.order_by('date')[:10]
#     context_dict = {}
#
#
#
#     return render(request, 'login-page.html', context_dict)


def no_user_profile(request):

    if request.user.profile.researcher == None and request.user.profile.participant == None:

        return True
    else:
        return False

def login_success(request):

    # if request.user.profile.researcher == None and request.user.profile.participant == None:
    if no_user_profile(request) == True:

        if request.user.profile.typex == 'Researcher':

            return redirect("/part_finder/researcher_registration/")

        if request.user.profile.typex == 'Participant':

            return redirect("/part_finder/participant_registration/")

        # return redirect("complete_registration")
    else:
        return redirect("index")



#old complete reg
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










# Test Form
class ParticipantRegistration(SessionWizardView):
    template_name = "part_finder/participant_registration.html"


    def done(self, form_list, **kwargs):
        request = self.request

        form_data = process_form_data(form_list, request)


        return render_to_response('part_finder/done.html', {'form_data': form_data })


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


def experiment (request, experiment_name_slug):

    context_dict = {}

    try:
        experiment = Experiment.objects.get(slug=experiment_name_slug)
        context_dict['experiment_name'] = experiment.name


        experiment_list = Experiment.objects.filter(slug=experiment_name_slug)

        context_dict['single_experiment'] = experiment_list

        context_dict['experiment'] = experiment

    except Experiment.DoesNotExist:
        pass

    return render(request, 'part_finder/experiments.html', context_dict)

#add experiment form
@login_required
def add_experiment(request):



    if request.method == 'POST':
        form = ExperimentForm(request.POST)

        if form.is_valid():
            # par = participant_form.save()
            # profile = request.user.profile
            # profile.participant = par
            # profile.save()

            experiment = form.save(commit=False)
            res = request.user.profile.researcher
            experiment.researcher = res
            form.save()

            #
            # experiment = form.save(commit=False)
            # experiment.user = request.user
            # form.save()

            return index(request)
        else:
            print form.errors
    else:
        form = ExperimentForm()

    return render(request, 'part_finder/add_experiment.html', {'form':form})

#participant details form
def participant_details(request):

    if request.method == 'POST':
        form = ParticipantForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)
        else:
            print form.errors

    else:
        form = ParticipantForm

    return render(request, 'part_finder/participant_details.html', {'form':form})


#Researcher signup
def researcher_signup(request):
    if request.method == 'POST':
        researcherForm = ResearcherForm(request.POST)

        if researcherForm.is_valid():
            researcherForm.save(commit=True)

            return index(request)
        else:
            print researcherForm.errors

    else:
        researcherForm = ResearcherForm()

    return render(request, 'part_finder/researcher_signup.html', {'form': researcherForm})


