__author__ = 'patrickfrempong'
from django import template
from part_finder.views_search import *
from django.http import HttpResponse, request
from django.contrib.auth.models import User


register = template.Library()


@register.filter(name='get_part_valid')
def get_part_valid(experiment, request):
    # user = User
    check_part_pref_valid = participant_pref_filter(request, experiment)

    if check_part_pref_valid == 0:
        part_valid = True
    else:
        part_valid = False

    return part_valid