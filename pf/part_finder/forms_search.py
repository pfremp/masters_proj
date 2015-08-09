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
from autocomplete_light_registry import *

class RequirementForm (forms.ModelForm):


    class Meta():
        model = Requirement
        exclude = ('match','experiment',)



class MatchingDetailForm(autocomplete_light.ModelForm):
    # l = autocomplete_light.MultipleChoiceField('OsAutocomplete', required=False, label='Language(s) Required')
    # l = autocomplete_light.MultipleChoiceField('LangAutocomplete', required=False, label='Language(s) Required')
    min_age = forms.IntegerField(initial=1, required=False)
    max_age = forms.IntegerField(initial=99, required=False)
    min_height = forms.IntegerField(initial=0, label='Minimum Height (CM)', required=False)
    max_height = forms.IntegerField(initial=200, label='Maximum Height (CM)', required=False)
    min_weight = forms.IntegerField(initial=0, label='Minimum Weight (KG)', required=False)
    max_weight = forms.IntegerField(initial=200, label='Maximum Weight (KG)', required=False)
    # l = forms.CharField(max_length=128)

    # l = forms.CharField(max_length=128, label="Language(s) Required", help_text='Enter the required languages with a space between each language e.g "English French German".', initial="English ", required=False)
    l = autocomplete_light.MultipleChoiceField('OsAutocomplete', required=False, label='Language(s) Required', initial="English")
    # lang = autocomplete_light.MultipleChoiceField('OsAutocomplete', required=False, label='Language(s) Required')

    class Media:
        """
        We're currently using Media here, but that forced to move the
        javascript from the footer to the extrahead block ...

        So that example might change when this situation annoys someone a lot.
        """
        js = ('js/dependant_autocomplete.js',)

    class Meta():
        model = MatchingDetail
        # fields = ('language',)
        exclude = ('requirement',)






class GenderForm(forms.ModelForm):

    class Meta():
        model = Gender
        fields = ('gender',)

class AgeForm(forms.ModelForm):

    class Meta():
        model = Age
        fields = ('min_age', 'max_age')

class HeightForm(forms.ModelForm):

    class Meta():
        model = Height
        fields = ('height',)

class WeightForm(forms.ModelForm):

    class Meta():
        model = Weight
        fields = ('weight',)