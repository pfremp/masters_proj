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
        return self.min_age + "  " + self.max_age




