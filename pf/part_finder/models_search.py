__author__ = 'patrickfrempong'
from django.db import models
from datetime import date, datetime, timedelta
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from cities_light.models import City, Country,Region
import cities_light
from django.core import urlresolvers
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from smart_selects.db_fields import ChainedForeignKey
from part_finder.models import Experiment


# gender
class Gender(models.Model):
    GENDER = (('male', 'male'), ('female','female'))
    gender = models.CharField(max_length=128, choices=GENDER)

    def __unicode__(self):
        return self.gender

class Age(models.Model):
    min_age = models.IntegerField(null=False, default=1)
    max_age = models.IntegerField(null=False, default=1)

    def __unicode__(self):
        return self.min_age

class Height(models.Model):
    height = models.IntegerField(default=0, null=False)

    def __unicode__(self):
        return self.height

class Weight(models.Model):
    weight = models.IntegerField(default=0, null=False)

    def __unicode__(self):
        return self.weight



class Requirement(models.Model):
    CHOICES = (('NO','NO'),('YES','YES'))
    DEF = 'NO'
    match = models.BooleanField(default=False)
    student = models.CharField(max_length=128, null=False, choices=CHOICES, default=DEF)
    age = models.CharField(max_length=128, null=False, choices=CHOICES, default=DEF)
    language = models.CharField(max_length=128, null=False, choices=CHOICES, default=DEF)
    height = models.CharField(max_length=128, null=False, choices=CHOICES, default=DEF)
    weight = models.CharField(max_length=128, null=False, choices=CHOICES, default=DEF)
    gender = models.CharField(max_length=128, null=False, choices=CHOICES, default=DEF)
    experiment = models.ForeignKey(Experiment, null=False, default=DEF)

    def __unicode__(self):
        return self.experiment.name + " Requirement"


