__author__ = 'patrickfrempong'

from django import forms
from part_finder.models import Researcher,Experiment,Participant,  UserProfile
from django.contrib.auth.models import User
from datetime import date
from django.contrib.auth import get_user_model


# #user form superclass (common attrib)
# class UserForm(forms.ModelForm):
#     dob = forms.DateField(help_text="Date of Birth")
#     matric = forms.IntegerField(help_text="Matriculation No.")
#     institution = forms.CharField(help_text="Institution")
#     contactNo = forms.IntegerField(help_text="Contact Number")
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
    name = forms.CharField(max_length=128, help_text="Experiment Name")
    date = forms.DateField(required=False, help_text="Experiment Date")
    paidEvent = forms.BooleanField(help_text="Paid Event")
    location = forms.ChoiceField(choices=LOCATIONS, help_text="Location")
    noOfPartsWanted = forms.IntegerField(max_value=1000, help_text="Number of Participants")
    startTime = forms.TimeField(help_text="Start Time")
    endTime = forms.TimeField(help_text="End Time")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta():
        model = Experiment
        fields = ('name', 'date', 'paidEvent', 'location', 'noOfPartsWanted', 'startTime', 'endTime')


class ParticipantForm (forms.ModelForm):
    # participant = forms.ModelChoiceField(queryset=Participant.objects.all(), help_text="Username")

    address = forms.CharField(required=False, help_text="Address", max_length=128)

    occupation = forms.CharField(required=False, help_text="Occupation", max_length=128)
    marital = forms.CharField(required=False, help_text="Marital Status", max_length=128)
    gender = forms.CharField(required=False, help_text="Gender", max_length=128)
    ethnicity = forms.CharField(required=False, help_text="Ethnicity", max_length=128)
    religion = forms.CharField(required=False, help_text="Religion", max_length=128)

    height = forms.IntegerField(help_text="Height (cm)", required=False)
    weight = forms.IntegerField(help_text="Weight (cm)", required=False)

    max_distance = forms.IntegerField(help_text="Max Distance", required=False)
    online_only = forms.CharField(help_text="Online Only", max_length=128, required=False)
    paid_only = forms.CharField(help_text="Paid Only", max_length=128, required=False)
    email_notifications = forms.CharField(help_text="Email Notifications", max_length=128, required=False)


    class Meta():
        model = Participant
        fields = ('address', 'occupation', 'marital', 'gender', 'ethnicity', 'religion', 'height', 'weight', 'max_distance', 'online_only', 'paid_only', 'email_notifications')

class SignupForm(forms.Form):
    TYPES = (('Participant','Participant'),('Researcher','Researcher'))
    first_name = forms.CharField(max_length=35, label='First name')
    last_name = forms.CharField(max_length=35, label='Last name')
    type = forms.ChoiceField(choices=TYPES, label='Type')

    # dob = forms.DateField(help_text="Date of Birth")
    # matric = forms.IntegerField(help_text="Matriculation No.")
    # institution = forms.CharField(help_text="Institution")
    # contactNo = forms.IntegerField(help_text="Contact Number")
    # password = forms.CharField(max_length=30, help_text="Password")



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