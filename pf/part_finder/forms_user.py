__author__ = 'patrickfrempong'

from django import forms
from part_finder.models import Researcher,Experiment,Participant,  UserProfile, University, TimeSlot, TodoList, Payment_type,Payment, Is_paid, Currency, Application
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
from django.forms.extras.widgets import *

class PartGeneralUpdateForm (autocomplete_light.ModelForm):

    YN = (('Yes','Yes'),('No','No'))
    EDUCATION = (('School', 'School'),('SQ1', 'School Qualification1'), ('College','College') , ('University' , 'University'))
    UNI = (('GCU','GCU'),('UoG','UoG'))
    dob = forms.DateField(label="Date of Birth", widget=DateWidget(usel10n=True, bootstrap_version=3), required=False)
    contact_number = forms.IntegerField(required=False, label="Contact No")
    occupation = forms.CharField(required=False, label="Occupation", max_length=128)
    education = forms.ChoiceField(choices=EDUCATION, label="Level of Education", required=True)
    student = forms.BooleanField(label="Student", required=False)

    class Media:
        js = ('js/dependant_autocomplete.js',)

    class Meta():
        model = Participant
        fields = ('dob','country','region','city','contact_number','occupation','education', 'language', 'student')

class PartStudentUpdateForm (forms.ModelForm):
    YOS = (('1' , '1'), ('2' , '2'),('3' , '3'),('4' , '4'),('5' , '5'))
    university = forms.ModelChoiceField(label="University", queryset=University.objects.all(), required=False)
    course_name = forms.CharField(label="Course Name",max_length=128, required=False)
    year_of_study = forms.ChoiceField(choices=YOS, label="Year of Study", required=False)
    matric = forms.CharField(label="Matric", required=False)

    class Meta():
        model = Participant
        fields = ('university', 'course_name', 'year_of_study', 'matric')

class PartDemoUpdateForm (forms.ModelForm):
    SEX = (('Male','Male'), ('Female','Female'), ('PNTS','Prefer not to say'))
    #Demographic
    gender = forms.ChoiceField(choices=SEX, required=False, label="Gender")
    #Health information
    height = forms.IntegerField(label="Height (cm)", required=False)
    weight = forms.IntegerField(label="Weight (kg)", required=False)


    class Meta():
        model = Participant
        fields = ('gender', 'height', 'weight')


class PartPrefUpdateForm (forms.ModelForm):

    #preferences
    online_only = forms.BooleanField(label="Online Only", required=False, help_text="Only show online experiments.")
    paid_only = forms.BooleanField(label="Paid Only", required=False, help_text="Only show paid experiments.")
    # uni_only = forms.BooleanField(label="Uni Only", required=False, help_text="Only show university experiments.")
    my_uni_only = forms.BooleanField(label="My Uni Only", required=False, help_text="Only show experiments from my univerisy.")
    city_only = forms.BooleanField(label="City Only", required=False, help_text="Only show experiments from my city")
    eligible_only = forms.BooleanField(label="Eligible Only", required=False, help_text="Only show experiments that I am eligible for")

    class Meta():
        model = Participant
        fields = ('online_only', 'paid_only' , 'my_uni_only', 'eligible_only','city_only')

class UserAccountUpdateForm(forms.ModelForm):

    class Meta():
        model = User
        exclude = ('is_superuser', 'last_login', 'groups', 'user_permissions', 'is_staff', 'is_active', 'date_joined')

