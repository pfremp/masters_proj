__author__ = 'patrickfrempong'

from django import forms
from part_finder.models import Researcher,Experiment,Participant,  UserProfile, University, Locations
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


class UniversityForm(forms.ModelForm):
    name = forms.CharField(max_length=128)

    class Meta():
        model = University
        fields = ('name',)

class LocationFrom(forms.ModelForm):
    name = forms.CharField(max_length=128)

    class Meta():
        model = Locations
        fields = ('name',)


class ResearcherForm (forms.ModelForm):

   dob = forms.DateField(label="Date of Birth", widget=DateWidget(usel10n=True, bootstrap_version=3), required=False)
   matric = forms.IntegerField(label="Matriculation No.", required=True)
   institution = forms.CharField(label="Institution", max_length=128)
   contact_no = forms.IntegerField(label="Contact Number")
   department = forms.CharField(label="Department Name")

   class Meta():
        model = Researcher
        fields =  ('dob', 'matric', 'institution', 'contact_no', 'department')

class ExperimentForm (forms.ModelForm):
    PAYMENT_TYPE = (('Credits','Credits'),('Money','Money'))
    # LOCATIONS = Locations.objects.all()
    LOCATIONS = (('Glasgow','Glasgow'),('London','London'))
    PMT_TYPE = (('Total','Total'),('Hourly','Hourly'), ('N/A', 'N/A'))
    name = forms.CharField(max_length=128, label="Name", required=True)
    short_description = forms.CharField(max_length=128)
    long_description = forms.CharField(max_length=500)
    date = forms.DateField(required=False, label="Experiment Date", widget=DateWidget(usel10n=True, bootstrap_version=3))
    start_time = forms.TimeField(label="Start Time", widget=TimeWidget(usel10n=True, bootstrap_version=3))
    end_time = forms.TimeField(label="End Time", widget=TimeWidget(usel10n=True, bootstrap_version=3))
    duration = forms.FloatField(label="Duration (hours)")
    paid_event = forms.BooleanField(label="Paid Event", required=False)
    currency = forms.ChoiceField(label="Currency", choices=PAYMENT_TYPE)
    payment_amount = forms.FloatField(label="Payment Amount")
    pmt_type = forms.ChoiceField(label="Payment Type", choices=PMT_TYPE)
    location = forms.ModelChoiceField(label="Location", queryset=Locations.objects.all(), required=False)
    address = forms.CharField(label="Address")
    no_of_participants_wanted = forms.IntegerField(max_value=10, label="No of Participants Wanted")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta():
        model = Experiment
        fields = ('name','short_description','long_description', 'date', 'start_time', 'end_time','duration', 'paid_event','currency','pmt_type','payment_amount', 'location','address', 'no_of_participants_wanted', )


class ParticipantForm (forms.ModelForm):
    # participant = forms.ModelChoiceField(queryset=Participant.objects.all(), label="Username")

    YN = (('Yes','Yes'),('No','No'))
    SEX = (('Male','Male'), ('Female','Female'))
    UNI = (('GCU','GCU'),('UoG','UoG'))
    address_line_1 = forms.CharField(required=False, label="Address Line 1", max_length=128)
    address_line_2 = forms.CharField(required=False, label="Address Line 2", max_length=128)
    city = forms.CharField(required=False, label="City", max_length=128)
    postcode = forms.CharField(required=False, label="Postcode", max_length=128)
    contact_number = forms.IntegerField(required=False, label="Contact No")
    occupation = forms.CharField(required=False, label="Occupation", max_length=128)
    student = forms.BooleanField(label="Student", required=True)

    university = forms.ModelChoiceField(label="University", queryset=University.objects.all(), required=False)
    course_name = forms.CharField(label="Course Name",max_length=128)
    graduation_year = forms.IntegerField(label="Graduation Year")
    matric = forms.IntegerField(label="Matric")

    #Demographic
    gender = forms.CharField(required=False, label="Gender", max_length=128)
    ethnicity = forms.CharField(required=False, label="Ethnicity", max_length=128)
    religion = forms.CharField(required=False, label="Religion", max_length=128)

    #Health information
    height = forms.IntegerField(label="Height (cm)", required=False)
    weight = forms.IntegerField(label="Weight (cm)", required=False)

    #preferences
    max_distance = forms.IntegerField(label="Max Distance", required=False)
    uni_only = forms.BooleanField(label="Uni Experiments Only", required=False)
    online_only = forms.BooleanField(label="Online Only", required=False)
    paid_only = forms.BooleanField(label="Paid Only", required=False)
    email_notifications = forms.BooleanField(label="Email Notifications", required=False)


    class Meta():
        model = Participant
        fields = ('address_line_1', 'address_line_2', 'city', 'postcode', 'contact_number', 'occupation', 'student','university', 'course_name', 'graduation_year', 'matric', 'gender' , 'ethnicity', 'religion', 'height', 'weight', 'max_distance', 'uni_only', 'online_only', 'paid_only')




class PartDetailsForm (forms.ModelForm):

    YN = (('Yes','Yes'),('No','No'))

    UNI = (('GCU','GCU'),('UoG','UoG'))
    address_line_1 = forms.CharField(required=False, label="Address Line 1", max_length=128)
    address_line_2 = forms.CharField(required=False, label="Address Line 2", max_length=128)
    city = forms.CharField(required=False, label="City", max_length=128)
    postcode = forms.CharField(required=False, label="Postcode", max_length=128)
    contact_number = forms.IntegerField(required=False, label="Contact No")
    occupation = forms.CharField(required=False, label="Occupation", max_length=128)
    student = forms.BooleanField(label="Student", required=False)

    class Meta():
        model = Participant
        fields = ('address_line_1', 'address_line_2', 'city', 'postcode', 'contact_number', 'occupation', 'student')


class PartStudentForm (forms.ModelForm):

    # UNI = (('GCU','GCU'),('UoG','UoG'))
    UNI = University.objects.filter()
    university = forms.ModelChoiceField(label="University", queryset=University.objects.all(), required=False)
    course_name = forms.CharField(label="Course Name",max_length=128, required=False)
    year = forms.IntegerField(label="Year", required=False)
    matric = forms.IntegerField(label="Matric", required=False)

    class Meta():
        model = Participant
        fields = ('university', 'course_name', 'year', 'matric')

class PartDemoForm (forms.ModelForm):
    SEX = (('Male','Male'), ('Female','Female'))
    #Demographic
    gender = forms.ChoiceField(choices=SEX, required=False, label="Gender")
    ethnicity = forms.CharField(required=False, label="Ethnicity", max_length=128)
    religion = forms.CharField(required=False, label="Religion", max_length=128)

    #Health information
    height = forms.IntegerField(label="Height (cm)", required=False)
    weight = forms.IntegerField(label="Weight (cm)", required=False)


    class Meta():
        model = Participant
        fields = ('gender' , 'ethnicity', 'religion', 'height', 'weight')


class PartPrefForm (forms.ModelForm):

    #preferences
    max_distance = forms.IntegerField(label="Max Distance", required=False)
    uni_only = forms.BooleanField(label="Uni Experiments Only", required=False)
    online_only = forms.BooleanField(label="Online Only", required=False)
    paid_only = forms.BooleanField(label="Paid Only", required=False)
    email_notifications = forms.BooleanField(label="Email Notifications", required=False)

    class Meta():
        model = Participant
        fields = ('max_distance', 'uni_only', 'online_only', 'paid_only')







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
