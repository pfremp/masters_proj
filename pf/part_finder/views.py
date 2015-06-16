from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):

    context_dict = {'boldmessage' : "I am bold font from the context"}
    return render(request, 'part_finder/index.html', context_dict)