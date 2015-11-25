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
from django.core.exceptions import ValidationError
import datetime


# Education Levels
EDUCATION = (('HS', 'High School Level'),
             ('SCQF3', '  -Access 3 / Foundation Standard Grade'),
             ('SCQF4', '-Intermediate 1 / General Standard Grade'),
             ('SCQF5','-Intermediate 2 / Credit Standard Grade'),
             ('GCSE','-GCSE'),
             ('SCQF6' , '-Higher'),
             ('ALEVEL' , '-A Level'),
             ('SCQF7' , '-Advanced Higher'),
             ('College' , 'College Level'),
             ('HNC' , '-HNC'),
             ('HND' , '-HND'),
             ('HE' , 'University Level'),
             ('HE1' , '-Bachelors  Degree'),
             ('HE2' , '-Honours  Degree'),
             ('HE3' , '-Masters  Degree'),
             ('HE4' , '-Doctorates'))

SEX = (('Male','Male'), ('Female','Female'), ('PNTS','Prefer not to say'))

YOS = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'))


# Validate Int is grater than 1
def validate_gt1(value):
    if value <= 0:
        raise ValidationError('Cannot be less than 1')


# University
class University(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


# Researcher
class Researcher(models.Model):
    university = models.ForeignKey(University, blank=True, null=True)
    department = models.CharField(max_length=128, blank=True, null=True)
    contact_no = models.IntegerField(null=True, blank=True)
    url = models.URLField(max_length=128, blank=True)

    def __unicode__(self):
        return self.userprofile.user.username


# Languages
class Languages(models.Model):
    language = models.CharField(max_length=128)

    def __unicode__(self):
        return str(self.language) or u''


# Experiment
class Experiment(models.Model):
    name = models.CharField(max_length=65, blank=False)
    long_description = models.CharField(max_length=1000, default=" ")
    duration = models.IntegerField(default=0)
    address = models.CharField(max_length=128, blank=True)
    city = models.ForeignKey('cities_light.city', null=True, blank=True)
    researcher = models.ForeignKey(Researcher, related_name="experiment")
    url = models.URLField(blank=True)
    researcher_slug = models.SlugField(unique=False, null=True)
    slug = models.SlugField(unique=True, null=True)
    is_full = models.BooleanField(default=False)
    has_ended = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    online = models.BooleanField(default=False)
    student_only = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.researcher_slug = slugify(self.researcher)
        super(Experiment, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


# Participant
class Participant(models.Model):
    dob = models.DateField(("Date"), default=date.today, null=True)
    city = models.ForeignKey('cities_light.city', null=True, blank=True)
    contact_number = models.IntegerField(blank=True, null=True)
    occupation = models.CharField(max_length=128, blank=True)
    language = models.ManyToManyField(Languages, related_name='participant', blank=True, default=None)
    education = models.CharField(choices=EDUCATION, blank=True, max_length=1000)
    student = models.BooleanField(default=False, blank=True)

    # Student Information
    university = models.ForeignKey(University, blank=True, null=True)
    course_name = models.CharField(max_length=100, null=True, blank=True)
    year = models.IntegerField(null=True)
    matric = models.CharField(max_length=20, null=True)

    # Demographic information
    gender = models.CharField(max_length=128, blank=True, choices=SEX)
    # Health information
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True )

    # Preferences
    city_only = models.BooleanField(blank=True, default=False)
    my_uni_only = models.BooleanField(default=False, blank=True)
    online_only = models.BooleanField(default=False, blank=True)
    paid_only = models.BooleanField(default=False, blank=True)
    # email_notifications = models.BooleanField(default=False, blank=True)
    experiments = models.ManyToManyField(Experiment, blank=True, related_name="participants")
    eligible_only = models.BooleanField(default=False, blank=True)
    non_applied_only = models.BooleanField(default=False, blank=True)
    reg_2_completed = models.BooleanField(default=False, blank=True)

    def __unicode__(self):
        return self.userprofile.user.username


# User Profile
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', unique=True)
    typex = models.CharField("type", max_length=128, blank=False)
    participant = models.OneToOneField(Participant, blank=True, null=True, related_name='userprofile')
    researcher = models.OneToOneField(Researcher, blank=True, null=True, related_name='userprofile')

    def update_res (forms):
        researcher = forms
        researcher.save()

    def __unicode__(self):
        return self.user.username


# Timeslot
class TimeSlot(models.Model):
    date = models.DateField(("Date"), default=date.today, null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    no_of_parts = models.PositiveIntegerField(validators=[validate_gt1])
    current_parts = models.PositiveIntegerField(default=0)
    experiment = models.ForeignKey(Experiment, related_name='timeslot')
    is_full = models.BooleanField(default=False)

    def clean(self):
        # Validate date
        if self.date < datetime.date.today():
            raise ValidationError('Date cannot be in the past.')

    def __unicode__(self):
        return str(self.date) + " " + str(self.start_time) + " - " + str(self.end_time)


# Experiment Payment - is paid (yes/no)
class Is_paid(models.Model):
    is_paid = models.CharField(max_length=128, null=True)

    def __unicode__(self):
        return self.is_paid


# Currency - Credits, Voucher, Cash
class Currency(models.Model):
    currency = models.CharField(max_length=128, null=True)
    is_paid = models.ForeignKey(Is_paid, null=True)

    def __unicode__(self):
        return self.currency


# Payment Frequency - Total or Hourly
class Payment_type(models.Model):
    payment_type = models.CharField(max_length=128, null=True)
    currency = models.ForeignKey(Currency)

    def __unicode__(self):
        return self.payment_type


# Experiment Payment method :-
# Chained Fields, Is Paid,
class Payment(models.Model):
    is_paid = models.ForeignKey(Is_paid)
    currency = ChainedForeignKey(
        Currency,
        chained_field="is_paid",
        chained_model_field="is_paid",
        show_all=False,
        auto_choose=True
    )
    payment_type = ChainedForeignKey(Payment_type, chained_field="currency", chained_model_field="currency")
    amount = models.FloatField(null=True, blank=True)
    experiment = models.ForeignKey(Experiment, null=True, related_name='payment')

    def __unicode__(self):
        return str(self.amount)


# Experiment Application
class Application(models.Model):
    STATUS = (('Pending','Pending'),('Accepted','Accepted'),('Standby','Standby'))
    researcher = models.ForeignKey(Researcher, null=True, related_name="application")
    participant = models.ForeignKey(Participant, null=True, related_name="application")
    experiment = models.ForeignKey(Experiment, null=True, related_name="application")
    timeslot = models.ForeignKey(TimeSlot, null=True, related_name="application")
    status = models.CharField(max_length=100)

    def __unicode__(self):
        return self.experiment.name

