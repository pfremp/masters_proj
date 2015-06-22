from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import User
from django.db import models

#Counter that increments event ID.
EVENT_ID = 5
def eventIdCounter():
    global EVENT_ID
    EVENT_ID = EVENT_ID+1




class Researcher(models.Model):

    user = models.OneToOneField(User)
    name = models.CharField(max_length=128, default="Researcher Name")
    matric = models.CharField(max_length=128)


    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class Experiment(models.Model):
    # eventIdCounter()
    PAID_EVENT = (('Y','Yes'),('N','No'))
    DURATION = (('2','2 hours'))
    FMT = '%H:%M'
    name = models.CharField(max_length=128, blank=True)
    expId = models.CharField(max_length=128, unique=True, primary_key=True, default=EVENT_ID)
    date = models.DateField(("Date"), default=date.today, blank=True)
    paidEvent = models.CharField(max_length=128, choices=PAID_EVENT)
    location = models.CharField(max_length=128)
    noOfPartsWanted = models.IntegerField(default=0)
    endTime = models.TimeField(blank=True, null=True)
    startTime = models.TimeField(blank=True, null=True)
    researcher = models.ForeignKey(Researcher)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name



class Participant(models.Model):
    YN = (('Y','Yes'),('N','No'))
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    #User standard details
    name = models.CharField(max_length=128, default="Participant Name")
    picture = models.ImageField(upload_to='profile_images', blank=True)
    dob = models.DateField(("Date"),default=date.today, blank=True)
    matric = models.CharField(max_length=128)
    email = models.EmailField(blank=True)
    contactNo = models.IntegerField(max_length=128, blank=True)
    address = models.CharField(max_length=128)

    #Demographic informatuon
    occupation = models.CharField(max_length=128, blank=True)
    maritial = models.CharField(max_length=128, blank=True)
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
    experiment = models.ManyToManyField(Experiment, null=True, blank=True)





    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

