from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify

class Researcher(models.Model):
    INSTITUTIONS = (('Glasgow','University of Glasgow'),('Strathclyde','Strathclyde University'))
    user = models.OneToOneField(User)
    name = models.CharField(max_length=128, default="Researcher Name")
    matric = models.CharField(max_length=128)
    institution = models.CharField(choices=INSTITUTIONS, max_length=128, null=True, blank=True)


    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class Experiment(models.Model):
    # eventIdCounter()
    PAID_EVENT = (('Y','Yes'),('N','No'))
    DURATION = (('2','2 hours'))
    FMT = '%H:%M'

    name = models.CharField(max_length=128, blank=True)
    expId = models.AutoField(primary_key=True, unique=True)
    date = models.DateField(("Date"), default=date.today, blank=True)
    paidEvent = models.CharField(max_length=128, choices=PAID_EVENT)
    location = models.CharField(max_length=128)
    noOfPartsWanted = models.IntegerField()
    endTime = models.TimeField(blank=True, null=True)
    startTime = models.TimeField(blank=True, null=True)
    researcher = models.ForeignKey(Researcher, blank=True, null=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Experiment, self).save(*args, **kwargs)

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
    experiment = models.ManyToManyField(Experiment, null=True, blank=True)





    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

