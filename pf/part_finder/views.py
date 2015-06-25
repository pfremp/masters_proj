from django.shortcuts import render
from django.http import HttpResponse
from part_finder.models import Researcher, Experiment, Participant
from part_finder.forms import ExperimentForm, ParticipantForm, ResearcherForm

# Create your views here.


def index(request):

    experiments_list = Experiment.objects.order_by('date')[:10]
    context_dict = {'experiments' : experiments_list}



    return render(request, 'part_finder/index.html', context_dict)


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
def add_experiment(request):

    if request.method == 'POST':
        form = ExperimentForm(request.POST)

        if form.is_valid():
            experiment = form.save(commit=False)
            experiment.user = request.user
            form.save()

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