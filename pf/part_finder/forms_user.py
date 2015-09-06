__author__ = 'patrickfrempong'

from django import forms
from part_finder.models import Researcher,Experiment,Participant,  UserProfile, University, TimeSlot, Payment_type,Payment, Is_paid, Currency, Application
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


# Education Levels
EDUCATION = (('HS' , 'High School Level'),
             ('SCQF3', '  -Access 3 / Foundation Standard Grade'),
             ('SCQF4', '-Intermediate 1 / General Standard Grade'),
             ('SCQF5','-Intermediate 2 / Credit Standard Grade'),
             ('GCSE','-GCSE'),
             ('SCQF6' , '-Higher'),
             ('ALEVEL' , '-A Level'),
             ('SCQF7' , '-Advanced Higher'),
             ('College' , 'College Level'),
             ('HNC' , '-HNC'),
             ('HND' , '-HND'),
             ('HE' , 'University Level'),
             ('HE1' , '-Bachelors  Degree'),
             ('HE2' , '-Honours  Degree'),
             ('HE3' , '-Masters  Degree'),
             ('HE4' , '-Doctorates'))

SEX = (('Male','Male'), ('Female','Female'), ('PNTS','Prefer not to say'))

YOS = (('1' , '1'), ('2' , '2'),('3' , '3'),('4' , '4'),('5' , '5'))


# Signup form for django allauth
class SignupForm(forms.Form):
    TYPES = (('Participant','Participant'),('Researcher','Researcher'))
    first_name = forms.CharField(max_length=35, label='First name')
    last_name = forms.CharField(max_length=35, label='Last name')
    # type = forms.ChoiceField(choices=TYPES, label='Account Type', help_text="Select 'Participant' or 'Researcher'. ")
    type = forms.ChoiceField(choices=TYPES, widget=forms.RadioSelect, label='Account Type', help_text="Select 'Participant' or 'Researcher'. ", required=True)

    class Meta():
        model = UserProfile
        fields = ('first_name', 'last_name', 'type')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        type = self.cleaned_data['type']
        user.save()
        # Use the created 'user' to create a UserProfile
        userprofile = UserProfile(user=user, typex=type)
        userprofile.save()


# participant form1 - general details
class ParticipantForm1 (autocomplete_light.ModelForm):

    contact_number = forms.IntegerField(required=False, label="Contact No" , help_text="07712345678")
    student = forms.BooleanField(label="Student", required=False)
    dob = forms.DateField(label="Date of Birth", widget=DateWidget(usel10n=True, bootstrap_version=3), required=False)

    # class Media:
    #     js = ('js/dependant_autocomplete.js',)

    class Meta():
        model = Participant
        fields = ('city','contact_number','dob','student')


# participant form 2 - extra info used for matching experiments
class ParticipantForm2 (autocomplete_light.ModelForm):
    education = forms.ChoiceField(choices=EDUCATION, label="Level of Education", required=True)
    occupation = forms.CharField(required=False, label="Occupation", max_length=128)

    # university details
    course_name = forms.CharField(label="Course Name",max_length=128, required=False)
    year_of_study = forms.ChoiceField(choices=YOS, label="Year of Study", required=False)
    matric = forms.CharField(label="Matric", required=False)

    # Demographic
    gender = forms.ChoiceField(required=False, label="Gender", choices=SEX)

    # Health information
    height = forms.IntegerField(label="Height (CM)", required=False)
    weight = forms.IntegerField(label="Weight (KG)", required=False)

    # preferences
    online_only = forms.BooleanField(label="Online Only", required=False, help_text="Only show online experiments.")
    paid_only = forms.BooleanField(label="Paid Only", required=False, help_text="Only show paid experiments.")
    my_uni_only = forms.BooleanField(label="My Uni Only", required=False, help_text="Only show experiments from my univerisy.")
    city_only = forms.BooleanField(label="City Only", required=False, help_text="Only show experiments from my city")
    eligible_only = forms.BooleanField(label="Eligible Only", required=False, help_text="Only show experiments that I am eligible for")

    class Media:
        js = ('js/dependant_autocomplete.js',)

    class Meta():
        model = Participant
        fields = ('education','occupation','language', 'university', 'course_name', 'year_of_study', 'matric', 'gender' ,'height', 'weight', 'online_only', 'paid_only' , 'my_uni_only', 'eligible_only','city_only')


# Participant Update form - General Details
class PartGeneralUpdateForm (autocomplete_light.ModelForm):
    YN = (('Yes','Yes'),('No','No'))
    dob = forms.DateField(label="Date of Birth", widget=DateWidget(usel10n=True, bootstrap_version=3), required=False)
    contact_number = forms.IntegerField(required=False, label="Contact No")
    occupation = forms.CharField(required=False, label="Occupation", max_length=128)
    education = forms.ChoiceField(choices=EDUCATION, label="Level of Education", required=True)
    student = forms.BooleanField(label="Student", required=False)

    class Media:
        js = ('js/dependant_autocomplete.js',)

    class Meta():
        model = Participant
        fields = ('dob','city','contact_number','occupation','education', 'language', 'student')


# Participant Update form - Student Details
class PartStudentUpdateForm (autocomplete_light.ModelForm):
    course_name = forms.CharField(label="Course Name",max_length=128, required=False)
    year_of_study = forms.ChoiceField(choices=YOS, label="Year of Study", required=False)
    matric = forms.CharField(label="Matric", required=False)

    class Media:
        js = ('js/dependant_autocomplete.js',)

    class Meta():
        model = Participant
        fields = ('university', 'course_name', 'year_of_study', 'matric')


# Participant Update form - Demographic Details
class PartDemoUpdateForm (forms.ModelForm):
    SEX = (('Male','Male'), ('Female','Female'), ('PNTS','Prefer not to say'))
    # Demographic
    gender = forms.ChoiceField(choices=SEX, required=False, label="Gender")
    # Health information
    height = forms.IntegerField(label="Height (cm)", required=False)
    weight = forms.IntegerField(label="Weight (kg)", required=False)

    class Meta():
        model = Participant
        fields = ('gender', 'height', 'weight')


# Participant Update form - Preference Details
class PartPrefUpdateForm (forms.ModelForm):
    online_only = forms.BooleanField(label="Online Only", required=False, help_text="Only show online experiments.")
    paid_only = forms.BooleanField(label="Paid Only", required=False, help_text="Only show paid experiments.")
    my_uni_only = forms.BooleanField(label="My Uni Only", required=False, help_text="Only show experiments from my univerisy.")
    city_only = forms.BooleanField(label="City Only", required=False, help_text="Only show experiments from my city")
    eligible_only = forms.BooleanField(label="Eligible Only", required=False, help_text="Only show experiments that I am eligible for")
    non_applied_only = forms.BooleanField(label="Non Applied Experiments Only", required=False, help_text="Don't show listings for experiments you have already applied for")

    class Meta():
        model = Participant
        fields = ('online_only', 'paid_only' , 'my_uni_only', 'eligible_only','city_only', 'non_applied_only')


# Participant Update form - Preference Details (Non student)
class PartPrefUpdateFormNS (forms.ModelForm):
    online_only = forms.BooleanField(label="Online Only", required=False, help_text="Only show online experiments.")
    paid_only = forms.BooleanField(label="Paid Only", required=False, help_text="Only show paid experiments.")
    city_only = forms.BooleanField(label="City Only", required=False, help_text="Only show experiments from my city")
    eligible_only = forms.BooleanField(label="Eligible Only", required=False, help_text="Only show experiments that I am eligible for")
    non_applied_only = forms.BooleanField(label="Non Applied Experiments Only", required=False, help_text="Don't show listings for experiments you have already applied for")

    class Meta():
        model = Participant
        fields = ('online_only', 'paid_only' , 'eligible_only','city_only', 'non_applied_only')


# User account update form
class UserAccountUpdateForm(forms.ModelForm):

    class Meta():
        model = User
        exclude = ('is_superuser', 'last_login', 'groups', 'user_permissions', 'is_staff', 'is_active', 'date_joined')


# Researcher Details Form
class ResearcherForm (autocomplete_light.ModelForm):
    department = forms.CharField(label="Department Name", max_length=128)
    contact_no = forms.IntegerField(label="Contact Number", help_text="e.g. 07712345678")
    url = forms.CharField(label="URL (Format: http://yoursite.com)")

    class Meta():
        model = Researcher
        fields =  ('university','department', 'contact_no', 'url')
