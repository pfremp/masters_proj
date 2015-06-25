__author__ = 'patrickfrempong'

from django import forms
from part_finder.models import Researcher,Experiment,Participant
from django.contrib.auth.models import User
from datetime import date

#user form superclass (common attrib)
class UserForm(forms.ModelForm):
    firstName = forms.CharField(max_length=30, help_text="First Name")
    lastName = forms.CharField(max_length=30, help_text="Last Name")
    username = forms.CharField(max_length=30, help_text="Username")
    email = forms.EmailField(max_length=128, help_text="Email")
    dob = forms.DateField(help_text="Date of Birth")
    matric = forms.IntegerField(help_text="Matriculation No.")
    institution = forms.CharField(help_text="Institution")
    contactNo = forms.IntegerField(help_text="Contact Number")
    password = forms.CharField(max_length=30, help_text="Password")

    class Meta:
        model = Experiment
        fields = ('firstName', 'lastName', 'email', 'dob', 'matric', 'institution', 'contactNo', 'password')

class ResearcherForm (UserForm):
   department = forms.CharField(help_text="Department Name")

   class Meta(UserForm.Meta):
        model = Researcher
        fields = UserForm.Meta.fields + ('department',)

class ExperimentForm (forms.ModelForm):
    LOCATIONS = (('Gla','Glasgow'),('Ldn','London'))
    name = forms.CharField(max_length=128, help_text="Experiment Name")
    date = forms.DateField(required=False, help_text="Experiment Date")
    paidEvent = forms.BooleanField(help_text="Paid Event")
    locations = forms.CharField(max_length=128, help_text="Location")
    noOfPartsWanted = forms.IntegerField(max_value=1000, help_text="Number of Participants")
    startTime = forms.TimeField(help_text="Start Time")
    endTime = forms.TimeField(help_text="End Time")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta():
        model = Experiment
        fields = ('name', 'date', 'paidEvent', 'locations', 'noOfPartsWanted', 'startTime', 'endTime')


class ParticipantForm (UserForm):
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


    class Meta(UserForm.Meta):
        model = Participant
        fields = UserForm.Meta.fields + ('address', 'occupation', 'marital', 'gender', 'ethnicity', 'religion', 'height', 'weight', 'max_distance', 'online_only', 'paid_only', 'email_notifications')


# forms.IntegerField(max_length=128, help_text="Experiment ID")



# application class.
# foreign keys: participant, experiment
# see ifinder