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
    # This line is required. Links UserProfile to a User model instance.

    user = models.OneToOneField(User)
    name = models.CharField(max_length=128, default="Participant Name")
    # The additional attributes we wish to include.
    picture = models.ImageField(upload_to='profile_images', blank=True)

    dob = models.DateField(("Date"),default=date.today, blank=True)
    matric = models.CharField(max_length=128)
    email = models.EmailField(blank=True)
    contactNo = models.IntegerField(max_length=128, blank=True)
    address = models.CharField(max_length=128)
    experiment = models.ManyToManyField(Experiment)





    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

