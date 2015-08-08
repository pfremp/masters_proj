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



class Requirement(models.Model):
    CHOICES = (('0','NO'),('1','YES'))
    DEF = 'NO'
    match = models.BooleanField(default=False)
    student = models.CharField(max_length=128, null=False, choices=CHOICES)
    age = models.CharField(max_length=128, null=False, choices=CHOICES)
    language = models.CharField(max_length=128, null=False, choices=CHOICES)
    height = models.CharField(max_length=128, null=False, choices=CHOICES)
    weight = models.CharField(max_length=128, null=False, choices=CHOICES)
    gender = models.CharField(max_length=128, null=False, choices=CHOICES)
    experiment = models.ForeignKey(Experiment, null=False)

    def __unicode__(self):
        return self.experiment.name + " Requirement"

# gender
class Gender(models.Model):
    GENDER = (('male', 'male'), ('female','female'))
    gender = models.CharField(max_length=128, choices=GENDER)
    requirement = models.ForeignKey(Requirement, null=True, related_name='req_gender')

    def __unicode__(self):
        return self.gender

class Age(models.Model):
    min_age = models.IntegerField(null=False, default=1)
    max_age = models.IntegerField(null=False, default=1)
    requirement = models.ForeignKey(Requirement, null=True, related_name='req_age')

    def __unicode__(self):
        return self.min_age

class Height(models.Model):
    height = models.IntegerField(default=0, null=False)
    requirement = models.ForeignKey(Requirement, null=True, related_name='req_height')

    def __unicode__(self):
        return self.height

class Weight(models.Model):
    weight = models.IntegerField(default=0, null=False)
    requirement = models.ForeignKey(Requirement, null=True, related_name='req_weight')

    def __unicode__(self):
        return self.weight





