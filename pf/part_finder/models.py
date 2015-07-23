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



# #common user attributes
# class CommonUser(models.Model):
#     INSTITUTIONS = (('Glasgow','University of Glasgow'),('Strathclyde','Strathclyde University'))
#     dob = models.DateField(default=date.today)
#     matric = models.IntegerField()
#     institution = models.CharField(choices=INSTITUTIONS, max_length=128)
#     contactNo = models.IntegerField()
#
#     def __unicode__(self):  #For Python 2, use __str__ on Python 3
#         return self.matric

class University(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class Researcher(models.Model):
    # INSTITUTIONS = (('Glasgow','University of Glasgow'),('Strathclyde','Strathclyde University'))
    university = models.ForeignKey(University, blank=True, null=True)
    department = models.CharField(max_length=128, blank=True, null=True)
    contact_no = models.IntegerField()
    url = models.URLField(max_length=128, blank=True)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.userprofile.user.username
        # return self.department


class Experiment(models.Model):
    CURRENCY = (('Credits','Credits'),('Money','Money'))
    PMT_TYPE = (('Total','Total'),('Hourly','Hourly'), ('N/A', 'N/A'))
    name = models.CharField(max_length=128, blank=False)
    short_description = models.CharField(max_length=128, blank=True)
    long_description = models.CharField(max_length=500, blank=True)
    # date = models.DateField(("Date"), default=date.today, null=True)
    # start_time = models.TimeField(blank=True)
    # end_time = models.TimeField(blank=True)
    duration = models.FloatField(blank=True)
    # paid_event = models.BooleanField(default=False)
    # currency = models.CharField(max_length=100, choices=CURRENCY, blank=True)
    # payment_amount = models.FloatField(max_length=1000, blank=True)
    # pmt_type = models.CharField(max_length=128, choices=PMT_TYPE, blank=True)
    address = models.CharField(max_length=128, blank=True)
    # location = models.CharField(max_length=128, null=True)
    city = models.ForeignKey('cities_light.city', null=True)

    # no_of_participants_wanted = models.IntegerField(null=True, blank=True)
    language_req = models.CharField(max_length=128, blank=True)
    researcher = models.ForeignKey(Researcher, related_name="experiment")
    url = models.URLField(blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Experiment, self).save(*args, **kwargs)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name



class Participant(models.Model):
    YN = (('Yes','Yes'),('No','No'))
    SEX = (('Male','Male'), ('Female','Female'), ('PNTS','Prefer not to say'))
    EDUCATION = (('School', 'School'), ('College','College') , ('University' , 'University'))

    dob = models.DateField(("Date"), default=date.today, null=True)
    country = models.ForeignKey('cities_light.country', null=True)
    region = models.ForeignKey('cities_light.region', null=True)
    city = models.ForeignKey('cities_light.city', null=True)
    contact_number = models.IntegerField(max_length=128, blank=True, null=True)
    occupation = models.CharField(max_length=128, blank=True)
    lang = models.CharField(max_length=128, blank=True)
    education = models.CharField(choices=EDUCATION, blank=True, max_length=1000)
    student = models.BooleanField(default=False, blank=True)

    #Student Information
    university = models.ForeignKey(University, blank=True, null=True)
    course_name = models.CharField(max_length=100)
    year = models.IntegerField(null=True)
    matric = models.CharField(max_length=20, null=True)

    #Demographic informatuon
    gender = models.CharField(max_length=128, blank=True, choices=SEX)
    #Health information
    height = models.IntegerField(max_length=128, blank=True, null=True)
    weight = models.IntegerField(max_length=128, blank=True, null=True)

    #Preferences
    max_distance = models.IntegerField(max_length=128, blank=True, null=True)
    uni_only = models.BooleanField(default=False, blank=True)
    online_only = models.BooleanField(default=False, blank=True)
    # online_only = models.IntegerField(max_length=128, blank=True, null=True)
    paid_only = models.BooleanField(default=False, blank=True)
    email_notifications = models.BooleanField(default=False, blank=True)
    experiments = models.ManyToManyField(Experiment, null=True, blank=True, related_name="participants")

    def ID(self, obj):
        return obj.id


    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        # return self.userprofile.user.username
        return self.userprofile.user.username

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', unique=True)
    typex = models.CharField("type", max_length=128, blank=False)
    participant = models.OneToOneField(Participant, blank=True, null=True, related_name='userprofile')
    researcher = models.OneToOneField(Researcher, blank=True, null=True, related_name='userprofile')

    def update_res (forms):
        researcher = forms
        researcher.save()

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.user.username




class Application(models.Model):
    STATUS = (('Pending','Pending'),('Accepted','Accepted'),('Standby','Standby'))
    Researcher = models.OneToOneField(Researcher, null=True, related_name="application")
    Participant = models.OneToOneField(Participant, null=True, related_name="application")
    Experiment = models.OneToOneField(Experiment, null=True, related_name="application")
    status = models.CharField(max_length=100, choices=STATUS)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.Experiment.name







#TEST AUTO COMPLETE
class Dummy(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True)
    country = models.ForeignKey('cities_light.country')
    region = models.ForeignKey('cities_light.region')

    def __unicode__(self):
        return '%s %s' % (self.country, self.region)





class TodoList(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name



#Renames to time slot below
class TimeSlot(models.Model):

    # name = models.CharField(max_length=150, help_text="e.g. Buy milk, wash dog etc", null=True)
    date = models.DateField(("Date"), default=date.today, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    no_of_parts = models.IntegerField(blank=True, null=True)
    experiment = models.ForeignKey(Experiment, null=True)

    def __unicode__(self):
        return self.experiment.name


#Renames to time slot below
# class TodoItemxx(models.Model):
#
#     # name = models.CharField(max_length=150, help_text="e.g. Buy milk, wash dog etc", null=True)
#     date = models.DateField(("Date"), default=date.today, null=True)
#     start_time = models.TimeField(blank=True, null=True)
#     end_time = models.TimeField(blank=True, null=True)
#     no_of_parts = models.IntegerField(blank=True, null=True)
#     experiment = models.ForeignKey(Experiment, null=True)
#
#     def __unicode__(self):
#         return self.experiment.name

# class TimeSlot(models.Model):
#
#     # name = models.CharField(max_length=150, help_text="e.g. Buy milk, wash dog etc", null=True)
#     date = models.DateField(("Date"), default=date.today, null=True)
#     start_time = models.TimeField(blank=True, null=True)
#     end_time = models.TimeField(blank=True, null=True)
#     no_of_parts = models.IntegerField(blank=True, null=True)
#     experiment = models.ForeignKey(Experiment, null=True)
#
#     def __unicode__(self):
#         return self.experiment.name


##.name + " (" + str(self.experiment) + ")"




class Contact(models.Model):
    subject = models.CharField(max_length=100)
    sender = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.subject



#
# @python_2_unicode_compatible
# class NonAdminAddAnotherModel(models.Model):
#     name = models.CharField(max_length=100)
#     widgets = models.ManyToManyField('self', blank=True)
#
#     def get_absolute_url(self):
#         return urlresolvers.reverse(
#             'non_admin_add_another_model_update', args=(self.pk,))
#
#     def __str__(self):
#         return self.name


# class Continent(models.Model):
#     continent = models.CharField(max_length=128, null=True)
#
#     def __unicode__(self):
#         return self.continent
#
# class Country(models.Model):
#     country = models.CharField(max_length=128, null=True)
#     continent = models.ForeignKey(Continent)
#
#     def __unicode__(self):
#         return self.country
#
# class Area(models.Model):
#     area = models.CharField(max_length=128, null=True)
#     country = models.ForeignKey(Country)
#
#     def __unicode__(self):
#         return self.area
#
# class Location(models.Model):
#     continent = models.ForeignKey(Continent)
#     country = ChainedForeignKey(
#         Country,
#         chained_field="continent",
#         chained_model_field="continent",
#         show_all=False,
#         auto_choose=True
#     )
#     area = ChainedForeignKey(Area, chained_field="country", chained_model_field="country")
#     amount = models.IntegerField(null=True)
#     # street = models.CharField(max_length=100)
#     #
#     #



class Is_paid(models.Model):
    is_paid = models.CharField(max_length=128, null=True)

    def __unicode__(self):
        return self.is_paid

class Currency(models.Model):
    currency = models.CharField(max_length=128, null=True)
    is_paid = models.ForeignKey(Is_paid)

    def __unicode__(self):
        return self.currency

class Payment_type(models.Model):
    payment_type = models.CharField(max_length=128, null=True)
    currency = models.ForeignKey(Currency)

    def __unicode__(self):
        return self.payment_type

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
    amount = models.IntegerField(null=True)
    experiment = models.ForeignKey(Experiment, null=True, related_name='experiment')
    # street = models.CharField(max_length=100)