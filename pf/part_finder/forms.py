__author__ = 'patrickfrempong'

from django import forms
from part_finder.models import Researcher,Experiment,Participant


class ExperimentForm (forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Experiment Name")
    date = forms.DateField(required=False, help_text="Experiment Date")
    paidEvent = forms.CharField(max_length=128, help_text="Paid Event (Y or N)")
    locations = forms.CharField(max_length=128, help_text="Location")
    noOfPartsWanted = forms.IntegerField(max_value=1000, help_text="Number of Participants")
    startTime = forms.TimeField(required=False, help_text="Start Time")
    endTime = forms.TimeField(required=False, help_text="End Time")
    researcher = forms.ModelChoiceField(queryset=Researcher.objects.all(), help_text="Researcher Name")

    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Experiment
        fields = ('name', 'expId', 'date', 'paidEvent', 'locations', 'noOfPartsWanted', 'startTime', 'endTime', 'researcher')


class ParticipantForm (forms.ModelForm):
    # participant = forms.ModelChoiceField(queryset=Participant.objects.all(), help_text="Username")

    name = forms.CharField(max_length=128, help_text="Participant Name")
    picture = forms.ImageField(help_text="Upload Image", required=False)
    dob = forms.DateField(required=False, help_text="D.O.B")
    matric =forms.IntegerField(help_text="Matric No", required=False)
    email = forms.EmailField(required=True, help_text="Email")
    contactNo = forms.IntegerField(required=False, help_text="Contact No.")
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


    class Meta:
        model = Participant
        fields = ('user', 'name', 'picture', 'dob', 'matric', 'email', 'contactNo', 'address', 'occupation', 'marital', 'gender', 'ethnicity', 'religion', 'height', 'weight', 'max_distance', 'online_only', 'paid_only', 'email_notifications')


# forms.IntegerField(max_length=128, help_text="Experiment ID")