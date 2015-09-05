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
from part_finder.models import Experiment, Languages


GENDER = (('male', 'Male'), ('female','Female'))

# Experiemnt requirements :-
# Stores whether a particular requirement will be used for an experiment
class Requirement(models.Model):
    CHOICES = (('0','NO'),('1','YES'))
    DEF = 'NO'
    match = models.BooleanField(default=False)
    student = models.BooleanField(default=False)
    age = models.BooleanField(default=False)
    language = models.BooleanField(default=False)
    height = models.BooleanField(default=False)
    weight = models.BooleanField(default=False)
    gender = models.BooleanField(default=False)
    experiment = models.ForeignKey(Experiment, null=False, related_name="requirement")

    def __unicode__(self):
        return self.experiment.name + " Requirement"

# Experiment requirement details
# Stores the specific requirement details for an experiment
class MatchingDetail(models.Model):
    gender = models.CharField(max_length=128, choices=GENDER, blank=True)
    min_age = models.IntegerField(null=True, default=1, blank=True)
    max_age = models.IntegerField(null=True, default=100, blank=True)
    min_height = models.IntegerField(default=0, null=True, blank=True)
    max_height = models.IntegerField(default=0, null=True, blank=True)
    min_weight = models.IntegerField(default=0, null=True, blank=True)
    max_weight = models.IntegerField(default=0, null=True, blank=True)
    l = models.CharField(max_length=128, blank=True)
    requirement = models.ForeignKey(Requirement, null=True, related_name='matchdetail')

    def __unicode__(self):
        return self.requirement.experiment.name + " Match Details"





