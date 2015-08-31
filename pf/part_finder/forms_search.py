__author__ = 'patrickfrempong'
from django import forms
from part_finder.models import Researcher,Experiment,Participant,  UserProfile, University, TimeSlot, Payment_type,Payment, Is_paid, Currency, Application
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
from autocomplete_light_registry import *

# Requirment form
# Form will be displayed on "Add Experiment" page
class RequirementForm (forms.ModelForm):

    class Meta():
        model = Requirement
        exclude = ('match','experiment',)


# Form for matching details
# Specific details of experiment requirements will be captured here
class MatchingDetailForm(autocomplete_light.ModelForm):
    min_age = forms.IntegerField(initial=1, required=False)
    max_age = forms.IntegerField(initial=99, required=False)
    min_height = forms.IntegerField(initial=0, label='Minimum Height (CM)', required=False)
    max_height = forms.IntegerField(initial=200, label='Maximum Height (CM)', required=False)
    min_weight = forms.IntegerField(initial=0, label='Minimum Weight (KG)', required=False)
    max_weight = forms.IntegerField(initial=200, label='Maximum Weight (KG)', required=False)
    l = autocomplete_light.MultipleChoiceField('OsAutocomplete', required=False, label='Language(s) Required', help_text="Enter languages in addition to English required.")

    class Media:
        js = ('js/dependant_autocomplete.js',)

    class Meta():
        model = MatchingDetail
        exclude = ('requirement',)

