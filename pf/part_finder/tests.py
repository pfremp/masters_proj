# from django.test import TestCase
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pf.settings")
# from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.contrib.auth.models import User
from django.test import TestCase
import populate_pf
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from part_finder.models import TimeSlot, Experiment, University, Researcher, UserProfile
from part_finder.forms import TimeSlotForm, ExperimentForm
import datetime
from django.core.exceptions import ValidationError

# driver = webdriver.Firefox()
# driver.implicitly_wait(10) # seconds



# Tests for all models
class ModelTests(TestCase):

    # Setup Timeslot, Experiment and Researcher
    def setUp(self):
        populate_pf.populate()

        #user
        self.user = User.objects.get(username="fsmith")

        #User profile
        self.up = UserProfile.objects.get(user=self.user)

        # Create Experiment
        self.exp1 = Experiment.objects.create(name="Science Experiment", long_description="Long Des..", duration=60, address="George Square, Glasgow", url="http://google.com", city=None, researcher=self.up.researcher)

        # Timeslot
        self.ts = TimeSlot.objects.create(date=datetime.date(2016,12,12), start_time='12:00', end_time='14:00', no_of_parts=5, current_parts = 0, experiment = Experiment.objects.all()[0])


    # Test Historic Date - model
    def test_ts_historic_date_model(self):
        ts = TimeSlot(date=datetime.date(2016,12,12), start_time='12:00', end_time='14:00', no_of_parts=5, current_parts = 0, experiment = Experiment.objects.all()[0])
        self.assertIsNone(ts.full_clean())


    # Test timeslot number of participant - model
    def test_ts_parts_model(self):
        ts = TimeSlot(date=datetime.date(2016,12,12), start_time='12:00', end_time='14:00', no_of_parts=5, current_parts = 0, experiment = Experiment.objects.all()[0])
        self.assertIsNone(ts.full_clean())

    # Add experiment - model
    def test_add_exp_model(self):
        exp = Experiment.objects.create(name="Test Experiment", long_description="Long Des..", duration=60, address="George Square, Glasgow", url="http://google.com", city=None, researcher=self.up.researcher)
        self.assertIsNone(exp.full_clean(), True)


    # # Ensure timeslot has experiment
    # def test_timeslot_has_exp(self):
    #     timeslot = self.ts
    #
    #     timeslot.experiment=None
    #     self.assertRaises(ValidationError,  )
    #     print timeslot.experiment


# Tests for all forms
class FormTests(TestCase):


     # Setup Timeslot, Experiment and Researcher
    def setUp(self):
        populate_pf.populate()

        #user
        self.user = User.objects.get(username="fsmith")

        #User profile
        self.up = UserProfile.objects.get(user=self.user)

        # Create Experiment
        self.exp1 = Experiment.objects.create(name="Science Experiment", long_description="Long Des..", duration=60, address="George Square, Glasgow", url="http://google.com", city=None, researcher=self.up.researcher)


    # Test timeslots
    # Test Historic Date - form
    def test_ts_historic_date_form(self):
        ts = TimeSlot(date='2016-12-12', start_time='12:00', end_time='14:00', no_of_parts=5, current_parts = 0, experiment = Experiment.objects.all()[0])
        data = {'date': ts.date, 'start_time': ts.start_time, 'end_time': ts.end_time, 'no_of_parts': ts.no_of_parts, 'current_parts': ts.current_parts, 'experiment': ts.experiment}
        ts_form = TimeSlotForm(data=data)
        self.assertEqual(ts_form.is_valid(), True)

    # Test timeslot number of participants - form
    def test_ts_parts_form(self):
        ts = TimeSlot(date='2016-12-12', start_time='12:00', end_time='14:00', no_of_parts=5, current_parts = 0, experiment = Experiment.objects.all()[0])
        data = {'date': ts.date, 'start_time': ts.start_time, 'end_time': ts.end_time, 'no_of_parts': ts.no_of_parts, 'current_parts': ts.current_parts, 'experiment': ts.experiment}
        ts_form = TimeSlotForm(data=data)
        self.assertEqual(ts_form.is_valid(), True)

    # Add experiment - form
    def test_add_exp_form(self):
        exp = Experiment(name="Test Experiment", long_description="Long Des..", duration=60, address="George Square, Glasgow", city=None, url="")
        data = {'name': exp.name, 'long_description': exp.long_description, 'duration': exp.duration, 'address': exp.address, 'city': exp.city, 'url': exp.url}
        exp_form = ExperimentForm(data=data)
        self.assertEqual(exp_form.is_valid(), True)