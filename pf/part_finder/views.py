from django.shortcuts import render
from django.http import HttpResponse
from part_finder.models import Researcher, Experiment, Participant

# Create your views here.


def index(request):

    experiments_list = Experiment.objects.order_by('date')[:10]
    context_dict = {'experiments' : experiments_list}



    return render(request, 'part_finder/index.html', context_dict)