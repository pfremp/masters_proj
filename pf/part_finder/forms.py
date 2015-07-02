__author__ = 'patrickfrempong'

from django import forms
from part_finder.models import Researcher,Experiment,Participant,  UserProfile
from django.contrib.auth.models import User
from datetime import date
from django.contrib.auth import get_user_model
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget


# #user form superclass (common attrib)
# class UserForm(forms.ModelForm):
#     dob = forms.DateField(label="Date of Birth")
#     matric = forms.IntegerField(label="Matriculation No.")
#     institution = forms.CharField(label="Institution")
#     contactNo = forms.IntegerField(label="Contact Number")
#
#
#     class Meta:
#         model = Experiment
#         fields = ('dob', 'matric', 'institution', 'contactNo')

class ResearcherForm (forms.ModelForm):

   dob = forms.DateField(help_text="Date of Birth")
   matric = forms.IntegerField(help_text="Matriculation No.", required=True)
   institution = forms.CharField(help_text="Institution")
   contactNo = forms.IntegerField(help_text="Contact Number")
   department = forms.CharField(help_text="Department Name")

   class Meta():
        model = Researcher
        fields =  ('department', 'dob', 'matric', 'institution', 'contactNo')

class ExperimentForm (forms.ModelForm):
    LOCATIONS = (('Glasgow','Glasgow'),('London','London'))
    name = forms.CharField(max_length=128, label="Name", required=True)
    date = forms.DateField(required=False, label="Experiment Date", widget=DateWidget(usel10n=True, bootstrap_version=3))
    paidEvent = forms.BooleanField(label="Paid Event", required=False)
    location = forms.ChoiceField(choices=LOCATIONS, label="Location")
    noOfPartsWanted = forms.IntegerField(max_value=1000, label="No of Participants Wanted")
    startTime = forms.TimeField(label="Start Time", widget=TimeWidget(usel10n=True, bootstrap_version=3))
    endTime = forms.TimeField(label="End Time", widget=TimeWidget(usel10n=True, bootstrap_version=3))
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta():
        model = Experiment
        fields = ('name', 'date', 'paidEvent', 'location', 'noOfPartsWanted', 'startTime', 'endTime')


class ParticipantForm (forms.ModelForm):
    # participant = forms.ModelChoiceField(queryset=Participant.objects.all(), label="Username")

    address = forms.CharField(required=False, label="Address", max_length=128)

    occupation = forms.CharField(required=False, label="Occupation", max_length=128)
    marital = forms.CharField(required=False, label="Marital Status", max_length=128)
    gender = forms.CharField(required=False, label="Gender", max_length=128)
    ethnicity = forms.CharField(required=False, label="Ethnicity", max_length=128)
    religion = forms.CharField(required=False, label="Religion", max_length=128)

    height = forms.IntegerField(label="Height (cm)", required=False)
    weight = forms.IntegerField(label="Weight (cm)", required=False)

    max_distance = forms.IntegerField(label="Max Distance", required=False)
    online_only = forms.CharField(label="Online Only", max_length=128, required=False)
    paid_only = forms.CharField(label="Paid Only", max_length=128, required=False)
    email_notifications = forms.CharField(label="Email Notifications", max_length=128, required=False)


    class Meta():
        model = Participant
        fields = ('address', 'occupation', 'marital', 'gender', 'ethnicity', 'religion', 'height', 'weight', 'max_distance', 'online_only', 'paid_only', 'email_notifications')

class SignupForm(forms.Form):
    TYPES = (('Participant','Participant'),('Researcher','Researcher'))
    first_name = forms.CharField(max_length=35, label='First name')
    last_name = forms.CharField(max_length=35, label='Last name')
    type = forms.ChoiceField(choices=TYPES, label='Type')

    # dob = forms.DateField(label="Date of Birth")
    # matric = forms.IntegerField(label="Matriculation No.")
    # institution = forms.CharField(label="Institution")
    # contactNo = forms.IntegerField(label="Contact Number")
    # password = forms.CharField(max_length=30, label="Password")



    # class Meta:
    #     model = get_user_model()

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        type = self.cleaned_data['type']
        # type = UserProfile.objects.get_or_create(user=user, typex=type)
        # Save the default User fields first, so you can get the User instance
        user.save()
        # Use the created 'user' to create a UserProfile
        userprofile = UserProfile(user=user, typex=type)
        userprofile.save()


# application class.
# foreign keys: participant, experiment
# see ifinder