from django.db import models
from datetime import date, datetime, timedelta
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify




# #common user attributes
# class CommonUser(models.Model):
#     INSTITUTIONS = (('Glasgow','University of Glasgow'),('Strathclyde','Strathclyde University'))
#     dob = models.DateField(default=date.today)
#     matric = models.IntegerField()
#     institution = models.CharField(choices=INSTITUTIONS, max_length=128)
#     contactNo = models.IntegerField()
#
#     def __unicode__(self):  #For Python 2, use __str__ on Python 3
#         return self.matric

class University(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class Locations(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class Researcher(models.Model):
    # INSTITUTIONS = (('Glasgow','University of Glasgow'),('Strathclyde','Strathclyde University'))
    dob = models.DateField(("Date"), default=date.today, null=True)
    institution = models.CharField(max_length=128, blank=True, null=True)
    contact_no = models.IntegerField()
    department = models.CharField(max_length=128, blank=True)


    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.userprofile.user.username


class Experiment(models.Model):
    CURRENCY = (('Credits','Credits'),('Money','Money'))
    PMT_TYPE = (('Total','Total'),('Hourly','Hourly'), ('N/A', 'N/A'))
    name = models.CharField(max_length=128, blank=False)
    short_description = models.CharField(max_length=128, blank=True)
    long_description = models.CharField(max_length=500, blank=True)
    date = models.DateField(("Date"), default=date.today)
    start_time = models.TimeField(blank=True)
    end_time = models.TimeField(blank=True)
    duration = models.FloatField(blank=True)
    paid_event = models.BooleanField(default=False)
    currency = models.CharField(max_length=100, choices=CURRENCY, blank=True)
    payment_amount = models.FloatField(max_length=1000, blank=True)
    pmt_type = models.CharField(max_length=128, choices=PMT_TYPE, blank=True)
    location = models.CharField(max_length=128)
    address = models.CharField(max_length=128, blank=True)
    no_of_participants_wanted = models.IntegerField(null=True, blank=True)
    researcher = models.ForeignKey(Researcher, related_name="experiment")
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Experiment, self).save(*args, **kwargs)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name



class Participant(models.Model):
    YN = (('Yes','Yes'),('No','No'))
    SEX = (('Male','Male'), ('Female','Female'))
    #User standard details

    address_line_1 = models.CharField(max_length=128, blank=True)
    address_line_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=128, blank=True)
    postcode = models.CharField(max_length=128, blank=True)
    contact_number = models.IntegerField(max_length=128, blank=True, null=True)
    occupation = models.CharField(max_length=128, blank=True)
    student = models.BooleanField(default=False, blank=True)

    #Student Information
    university = models.ForeignKey(University, blank=True, null=True)
    course_name = models.CharField(max_length=100)
    year = models.IntegerField(null=True)
    matric = models.CharField(max_length=20, null=True)

    #Demographic informatuon
    gender = models.CharField(max_length=128, blank=True, choices=SEX)
    ethnicity = models.CharField(max_length=128, blank=True)
    religion = models.CharField(max_length=128, blank=True)

    #Health information
    height = models.IntegerField(max_length=128, blank=True, null=True)
    weight = models.IntegerField(max_length=128, blank=True, null=True)

    #Preferences
    max_distance = models.IntegerField(max_length=128, blank=True, null=True)
    uni_only = models.BooleanField(default=False, blank=True)
    online_only = models.BooleanField(default=False, blank=True)
    # online_only = models.IntegerField(max_length=128, blank=True, null=True)
    paid_only = models.BooleanField(default=False, blank=True)
    email_notifications = models.BooleanField(default=False, blank=True)
    experiments = models.ManyToManyField(Experiment, null=True, blank=True, related_name="participants")

    def ID(self, obj):
        return obj.id


    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        # return self.userprofile.user.username
        return self.userprofile.user.username

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', unique=True)
    typex = models.CharField("type", max_length=128, blank=False)
    participant = models.OneToOneField(Participant, blank=True, null=True, related_name='userprofile')
    researcher = models.OneToOneField(Researcher, blank=True, null=True, related_name='userprofile')

    def update_res (forms):
        researcher = forms
        researcher.save()

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.user.username


class Contact(models.Model):
    subject = models.CharField(max_length=100)
    sender = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.subject

class Application(models.Model):
    STATUS = (('Pending','Pending'),('Accepted','Accepted'),('Standby','Standby'))
    Researcher = models.OneToOneField(Researcher, null=True, related_name="application")
    Participant = models.OneToOneField(Participant, null=True, related_name="application")
    Experiment = models.OneToOneField(Experiment, null=True, related_name="application")
    status = models.CharField(max_length=100, choices=STATUS)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.Experiment.name