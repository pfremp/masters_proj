from django.db import models
from datetime import date

# Create your models here.

#Experiment model

class Experiment(models.Model):
    name = models.CharField(max_length=128)
    id = models.CharField(max_length=128)
    date = models.DateField(("Date"), default=date.today)
    eventStatus = models.CharField(max_length=128)
    paidEvent = models.CharField(max_length=128)
    startTime = models.TimeField()
    location = models.CharField(max_length=128)
    ManagerId = models.IntegerField(default=000)
    duration = models.IntegerField(default=000)
    NoOfPartsWanted = models.IntegerField(default=000)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

# ß
