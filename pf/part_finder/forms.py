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
from django.core.exceptions import ValidationError
import datetime
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import SplitDateTimeWidget




# Validators

# Validate Date - experiment date cannot be a historic date
def validate_date(date):
    if date < datetime.date.today():
        raise ValidationError('Date cannot be a date in the past.')

# Validate Int is grater than 1
def validate_gt1(value):
    if value < 0:
        raise ValidationError('Cannot be less than 1')


# Experiment Form
class ExperimentForm (autocomplete_light.ModelForm):
    name = forms.CharField(max_length=128, label="Experiment Name", required=True)
    long_description = forms.CharField(label="Description", max_length=600, widget=forms.Textarea)
    city = autocomplete_light.ModelChoiceField('CityAutocompleteCity', required=False, label='Location')
    address = forms.CharField(label="Address", required=False, help_text="Enter the full address of the experiment, this will be used for the google map display. e.g. 1 George St, Glasgow, G2 1DU.")
    duration = forms.FloatField(label="Duration (Mins)", required=True, help_text="Enter how long the experiment will last in minutes e.g. 1.5 hours = 90 mins")
    url = forms.URLField(max_length=200, required=False, label='URL: http://yoursite.com', initial="http://")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Media:
        js = ('js/dependant_autocomplete.js',)

    class Meta():
        model = Experiment
        fields = ('name', 'long_description','duration', 'city','address', 'url')


# Experiment timeslot form
class TimeSlotForm(ModelForm):
    CHOICES = (('choice','choice'),('choice1','choice1') )
    date = forms.DateField(required=False, label="Experiment Date (DD/MM/YYYY)", initial=date.today(), validators=[validate_date], widget=SelectDateWidget)
    start_time = forms.TimeField(label="Start Time (HH:MM)", required=False, help_text="Please enter the start time using the 24hr format. e.g. 2.30pm = 14:30")
    end_time = forms.TimeField(label="End Time (HH:MM)", required=False, help_text="Please enter the start time using the 24hr format. e.g. 2.30pm = 14:30")
    no_of_parts = forms.IntegerField(label="No of Participants Required", required=False, validators=[validate_gt1])

    class Meta:
        model = TimeSlot
        fields = ('date', 'start_time', 'end_time', 'no_of_parts',)


# Payment form
class PaymentForm(forms.ModelForm):
    currency = forms.ModelChoiceField(label="Currency", queryset=Currency.objects.all(), required=False, help_text="Cash, University Credits or Voucher")
    amount = forms.FloatField(label="Payment Amount (GBP)", required=False, help_text="Payment amonut in British Pounds")

    class Meta:
        model = Payment
        fields = ('is_paid','currency', 'payment_type', 'amount')
        exclude = ('experiment',)


# Experiment application form
class ApplicationForm(forms.ModelForm):

    def __init__(self, experiment, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.fields['timeslot'].queryset = TimeSlot.objects.filter(experiment=experiment, is_full=False)

    class Meta:
        model = Application
        fields = ('timeslot',)


# Experiment form to update status
class UpdateStatusForm(forms.ModelForm):
    STATUS = (('',''), ('Pending','Pending'),('Accepted','Accepted'),('Standby','Standby'),('Cancelled','Cancelled'),('Unsuccessful', 'Unsuccessful'))
    status = forms.ChoiceField(label="Update Status", required=True, choices=STATUS, help_text="Select a status and click update")

    class Meta:
        model = Application
        fields = ('status',)


# Experiment form to update status (for full experiments)
class UpdateStatusFormFull(forms.ModelForm):
    STATUS = (('',''), ('Pending','Pending'), ('Standby','Standby'),('Cancelled','Cancelled'), ('Unsuccessful', 'Unsuccessful'))
    status = forms.ChoiceField(label="Update Status", required=True, choices=STATUS, help_text="Select a status and click update")

    class Meta:
        model = Application
        fields = ('status',)



