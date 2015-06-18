from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.title

    class Meta:
        ordering = ('title',)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication, blank=True)

    def __unicode__(self):             # __unicode__ on Python 2
        return self.headline

    class Meta:
        ordering = ('headline',)


