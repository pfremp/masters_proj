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

# class UniversityForm(forms.ModelForm):
#     name = forms.CharField(max_length=128)
#
#     class Meta():
#         model = University
#         fields = ('name',)


class ResearcherForm (forms.ModelForm):
   university = forms.ModelChoiceField(label="University", queryset=University.objects.all(), required=False)
   department = forms.CharField(label="Department Name", max_length=128)
   contact_no = forms.IntegerField(label="Contact Number")
   url = forms.CharField(label="URL (Format: http://yoursite.com)")

   class Meta():
        model = Researcher
        fields =  ('university','department', 'contact_no', 'url')

class ExperimentForm (forms.ModelForm):
    PAYMENT_TYPE = (('Credits','Credits'),('Money','Money'))
    LOCATIONS = (('Glasgow','Glasgow'),('London','London'))
    PMT_TYPE = (('Total','Total'),('Hourly','Hourly'), ('N/A', 'N/A'))
    name = forms.CharField(max_length=128, label="Name", required=True)
    short_description = forms.CharField(max_length=128)
    long_description = forms.CharField(max_length=500, widget=forms.Textarea)
    city = autocomplete_light.ModelChoiceField('CityAutocompleteCity', required=False, label='Location')
    address = forms.CharField(label="Address")
    language_req = autocomplete_light.MultipleChoiceField('OsAutocomplete', required=False, label='Language(s) Required')
    url = forms.URLField(max_length=200, required=False)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Media:
        """
        We're currently using Media here, but that forced to move the
        javascript from the footer to the extrahead block ...

        So that example might change when this situation annoys someone a lot.
        """
        js = ('js/dependant_autocomplete.js',)


    class Meta():
        model = Experiment
        fields = ('name','short_description','long_description','duration', 'city','address', 'language_req' )


class ParticipantForm (autocomplete_light.ModelForm):
    SEX = (('Male','Male'), ('Female','Female'), ('PNTS','Prefer not to say'))
    UNI = (('GCU','GCU'),('UoG','UoG'))
    EDUCATION = (('School', 'School'),('SQ1', 'School Qualification1'), ('College','College') , ('University' , 'University'))
    YOS = (('1' , '1'), ('2' , '2'),('3' , '3'),('4' , '4'),('5' , '5'))

    dob = forms.DateField(label="Date of Birth", widget=DateWidget(usel10n=True, bootstrap_version=3), required=False)
    contact_number = forms.IntegerField(required=False, label="Contact No")
    occupation = forms.CharField(required=False, label="Occupation", max_length=128)
    education = forms.ChoiceField(choices=EDUCATION, label="Level of Education", required=True)
    student = forms.BooleanField(label="Student", required=False)
    lang = autocomplete_light.MultipleChoiceField('OsAutocomplete', required=False, label='Languages')

    university = forms.ModelChoiceField(label="University", queryset=University.objects.all(), required=False)
    course_name = forms.CharField(label="Course Name",max_length=128, required=False)
    year_of_study = forms.ChoiceField(choices=YOS, label="Year of Study", required=False)
    matric = forms.CharField(label="Matric", required=False)

    #Demographic
    gender = forms.CharField(required=False, label="Gender", max_length=128)


    #Health information
    height = forms.IntegerField(label="Height (cm)", required=False)
    weight = forms.IntegerField(label="Weight (cm)", required=False)

    #preferences
    max_distance = forms.IntegerField(label="Max Distance", required=False)
    uni_only = forms.BooleanField(label="Uni Experiments Only", required=False)
    online_only = forms.BooleanField(label="Online Only", required=False)
    paid_only = forms.BooleanField(label="Paid Only", required=False)
    email_notifications = forms.BooleanField(label="Email Notifications", required=False)

    class Media:
        """
        We're currently using Media here, but that forced to move the
        javascript from the footer to the extrahead block ...

        So that example might change when this situation annoys someone a lot.
        """
        js = ('js/dependant_autocomplete.js',)

    class Meta():
        model = Participant
        fields = ('dob','country','region','city','contact_number','occupation','education','student','lang','university', 'course_name', 'year_of_study', 'matric', 'gender' ,'height', 'weight', 'max_distance', 'uni_only', 'online_only', 'paid_only')




class PartDetailsForm (autocomplete_light.ModelForm):

    YN = (('Yes','Yes'),('No','No'))
    EDUCATION = (('School', 'School'),('SQ1', 'School Qualification1'), ('College','College') , ('University' , 'University'))
    UNI = (('GCU','GCU'),('UoG','UoG'))
    dob = forms.DateField(label="Date of Birth", widget=DateWidget(usel10n=True, bootstrap_version=3), required=False)
    contact_number = forms.IntegerField(required=False, label="Contact No")
    occupation = forms.CharField(required=False, label="Occupation", max_length=128)
    education = forms.ChoiceField(choices=EDUCATION, label="Level of Education", required=True)
    student = forms.BooleanField(label="Student", required=False)
    # lang = autocomplete_light.MultipleChoiceField('OsAutocomplete', required=False, label='Languages')
    lang = autocomplete_light.MultipleChoiceField('OsAutocomplete', required=False, label='Languages')

    class Media:
        """
        We're currently using Media here, but that forced to move the
        javascript from the footer to the extrahead block ...

        So that example might change when this situation annoys someone a lot.
        """
        js = ('js/dependant_autocomplete.js',)

    # class Meta:
    #     model = Participant
    #     exclude = []
    class Meta():
        model = Participant
        fields = ('dob','country','region','city','contact_number','occupation','education','lang')


class PartStudentForm (forms.ModelForm):
    YOS = (('1' , '1'), ('2' , '2'),('3' , '3'),('4' , '4'),('5' , '5'))
    university = forms.ModelChoiceField(label="University", queryset=University.objects.all(), required=False)
    course_name = forms.CharField(label="Course Name",max_length=128, required=False)
    year_of_study = forms.ChoiceField(choices=YOS, label="Year of Study", required=False)
    matric = forms.CharField(label="Matric", required=False)

    class Meta():
        model = Participant
        fields = ('university', 'course_name', 'year_of_study', 'matric')

class PartDemoForm (forms.ModelForm):
    SEX = (('Male','Male'), ('Female','Female'), ('PNTS','Prefer not to say'))
    #Demographic
    gender = forms.ChoiceField(choices=SEX, required=False, label="Gender")
    #Health information
    height = forms.IntegerField(label="Height (cm)", required=False)
    weight = forms.IntegerField(label="Weight (kg)", required=False)


    class Meta():
        model = Participant
        fields = ('gender', 'height', 'weight')


class PartPrefForm (forms.ModelForm):

    #preferences
    max_distance = forms.IntegerField(label="Max Distance", required=False)
    uni_only = forms.BooleanField(label="Uni Experiments Only", required=False)
    online_only = forms.BooleanField(label="Online Only", required=False)
    paid_only = forms.BooleanField(label="Paid Only", required=False)
    email_notifications = forms.BooleanField(label="Email Notifications", required=False)

    class Meta():
        model = Participant
        fields = ('max_distance', 'uni_only', 'online_only', 'paid_only','email_notifications')


class SignupForm(forms.Form):
    TYPES = (('Participant','Participant'),('Researcher','Researcher'))
    first_name = forms.CharField(max_length=35, label='First name')
    last_name = forms.CharField(max_length=35, label='Last name')
    type = forms.ChoiceField(choices=TYPES, label='Type')

    class Meta():
        model = UserProfile
        fields = ('first_name', 'last_name', 'type')

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


class TimeSlotForm(ModelForm):
    CHOICES = (('choice','choice'),('choice1','choice1') )
    date = forms.DateField(required=False, label="Experiment Date (YYYY-MM-DD)")
    start_time = forms.TimeField(label="Start Time (HH:MM)", required=False)
    end_time = forms.TimeField(label="End Time (HH:MM)", required=False)
    no_of_parts = forms.IntegerField(label="No of Participants Wanted", required=False)

    class Meta:
        model = TimeSlot
        fields = ('date', 'start_time', 'end_time', 'no_of_parts',)
        # exclude = ('experiment',)

class PaymentForm(forms.ModelForm):
    # is_paid = forms.CharField(label="Paid Experiment", required=False)
    # currency = forms.ModelChoiceField(label="Currency", queryset=Currency.objects.all(), required=False)
    # payment_type = forms.ModelChoiceField(label="Payment Type", queryset=Payment_type.objects.all(), required=False)
    # amount = forms.IntegerField(label="Payment Amount", required=False)

    class Meta:
        model = Payment
        fields = ('is_paid','currency', 'payment_type', 'amount')
        exclude = ('experiment',)

class ApplicationForm(forms.ModelForm):
    YES = (('Yes','Yes'), (' ',' '))
    # timeslot = forms.ModelChoiceField(queryset=TimeSlot.objects.all(), label="Select Timeslot", required=False)
    terms = forms.BooleanField(label="Terms Accepted", required=True, help_text='You must accept the T&Cs to proceed.')


    def __init__(self, experiment, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.fields['timeslot'].queryset = TimeSlot.objects.filter(experiment=experiment, is_full=False)
        # self.fields['terms'].required=True

    class Meta:
        model = Application
        fields = ('timeslot' , 'terms')
        # exclude = ('researcher', 'participant', 'experiment', 'status')
        # exclude = ()

class UpdateStatusForm(forms.ModelForm):
    STATUS = (('',''), ('Pending','Pending'),('Accepted','Accepted'),('Standby','Standby'),('Cancelled','Cancelled'),('Unsuccessful', 'Unsuccessful'))
    status = forms.ChoiceField(label="Update Status", required=True, choices=STATUS, help_text="Select a status and click update")

    class Meta:
        model = Application
        fields = ('status',)

class UpdateStatusFormFull(forms.ModelForm):
    STATUS = (('',''), ('Pending','Pending'), ('Standby','Standby'),('Cancelled','Cancelled'), ('Unsuccessful', 'Unsuccessful'))
    status = forms.ChoiceField(label="Update Status", required=True, choices=STATUS, help_text="Select a status and click update")

    class Meta:
        model = Application
        fields = ('status',)



# class ApplicationForm(forms.ModelForm):

# application class.
# foreign keys: participant, experiment
# see ifinder


#
# class ContactForm1(forms.Form):
#     subject = forms.CharField(max_length=100)
#     sender = forms.EmailField()
#
#     class Meta():
#         model = Contact
#         fields = ('subject', 'sender')
#
#
# class ContactForm2(forms.Form):
#     message = forms.CharField(widget=forms.Textarea)
#
#     class Meta():
#         model = Contact
#         fields = ('message')

#
# NonAdminAddAnotherModelForm = al.modelform_factory(NonAdminAddAnotherModel,
#         exclude=[])


class TimeSlotFrom(ModelForm):
  class Meta:
    model = TodoList
    exclude = ('',)

