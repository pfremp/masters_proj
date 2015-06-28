from django.db import models
from datetime import date, datetime
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

class Researcher(models.Model):
    INSTITUTIONS = (('Glasgow','University of Glasgow'),('Strathclyde','Strathclyde University'))
    dob = models.DateField(default=date.today)
    matric = models.IntegerField()
    institution = models.CharField(choices=INSTITUTIONS, max_length=128)
    contactNo = models.IntegerField()
    department = models.CharField(max_length=128, blank=True)


    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.userprofile.user.username


class Experiment(models.Model):
    # eventIdCounter()
    PAID_EVENT = (('Y','Yes'),('N','No'))
    DURATION = (('2','2 hours'))
    LOCATIONS = (('Glasgow','Glasgow'),('London','London'))
    FMT = '%H:%M'

    name = models.CharField(max_length=128, blank=False)
    date = models.DateField(("Date"), default=date.today)
    paidEvent = models.BooleanField(default=False)
    location = models.CharField(max_length=128, choices=LOCATIONS)
    noOfPartsWanted = models.IntegerField(null=True)
    endTime = models.TimeField(blank=True)
    startTime = models.TimeField(blank=True)
    researcher = models.ForeignKey(Researcher, related_name="experiment")
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Experiment, self).save(*args, **kwargs)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name



class Participant(models.Model):
    YN = (('Y','Yes'),('N','No'))
    #User standard details
    address = models.CharField(max_length=128)

    #Demographic informatuon
    occupation = models.CharField(max_length=128, blank=True)
    marital = models.CharField(max_length=128, blank=True)
    gender = models.CharField(max_length=128, blank=True)
    ethnicity = models.CharField(max_length=128, blank=True)
    religion = models.CharField(max_length=128, blank=True)

    #Health information
    height = models.IntegerField(max_length=128, blank=True, null=True)
    weight = models.IntegerField(max_length=128, blank=True, null=True)

    #Preferences
    max_distance = models.IntegerField(max_length=128, blank=True, null=True)
    online_only = models.IntegerField(max_length=128, blank=True, null=True)
    paid_only = models.CharField(max_length=128, blank=True, choices=YN)
    email_notifications = models.CharField(max_length=128, blank=True, choices=YN)
    experiments = models.ManyToManyField(Experiment, null=True, blank=True, related_name="participants")

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.userprofile.user.username


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', unique=True)
    typex = models.CharField("type", max_length=128, blank=False)
    participant = models.OneToOneField(Participant, blank=True, null=True)
    researcher = models.OneToOneField(Researcher, blank=True, null=True)

    def update_res (forms):
        researcher = forms
        researcher.save()

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.user.username