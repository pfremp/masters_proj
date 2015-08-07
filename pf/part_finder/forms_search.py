__author__ = 'patrickfrempong'
from django import forms
from part_finder.models import Researcher,Experiment,Participant,  UserProfile, University, TimeSlot, TodoList, Payment_type,Payment, Is_paid, Currency, Application
from part_finder.models_search import *
from django.contrib.auth.models import User
from datetime import date
from django.contrib.auth import get_user_model
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget
from cities_light.models import City, Country
import cities_light
import autocomplete_light
# from .models import NonAdminAddAnotherModel
import autocomplete_light.shortcuts as al

from django.forms import ModelForm
from smart_selects.db_fields import GroupedForeignKey


class RequirementForm (forms.ModelForm):

   class Meta():
        model = Requirement
        exclude =  ('match','experiment',)