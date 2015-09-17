# from django.test import TestCase
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pf.settings")
from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.contrib.auth.models import User
from django.test import TestCase
import populate_pf
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from part_finder.models import TimeSlot, Experiment, University, Researcher, UserProfile, Participant, Languages
from part_finder.forms import TimeSlotForm, ExperimentForm
from part_finder.models_search import Requirement, MatchingDetail
from part_finder.views_user import refresh_reqs
from part_finder.views_search import check_applicant_validity, match_gender, match_age, match_height, match_lang, match_weight
import datetime
from django.http import HttpResponse, request, HttpRequest
from django.contrib.auth.models import User
import datetime


from django.core.exceptions import ValidationError

# driver = webdriver.Firefox()
# driver.implicitly_wait(10) # seconds


class ViewTests(TestCase):

    def setUp(self):
        populate_pf.populate()
        self.participant = Participant.objects.all()[0]

        # print self.participant
        self.experiment = Experiment.objects.get(name="It's all in the face!")
        # print experiment.name
        self.requirement = Requirement.objects.get(experiment=self.experiment)
        # print requirement
        self.requirement_detail = MatchingDetail.objects.get(requirement=self.requirement)
        # print requirement_detail

        # set all requirements to false
        self.requirement.student=False
        self.requirement.age = False
        self.requirement.language = False
        self.requirement.height = False
        self.requirement.weight = False
        self.requirement.gender = False
        self.requirement.save()
        refresh_reqs(self.experiment)

    # Test if requirement's match boolean is updated to false when there are no experiments selected
    # or true when there is at least one requirement selected.
    def test_refresh_reqs(self):
        refresh_reqs(self.experiment)
        self.assertFalse(Requirement.objects.get(experiment=self.experiment).match)

    # Match will be set to true as the student requirement is set to true
    def test_refresh_reqs_true(self):
        self.requirement.student = True
        self.requirement.save()
        refresh_reqs(self.experiment)
        self.assertTrue(Requirement.objects.get(experiment=self.experiment).match)



# Test participant validity view
# Create participant
# Create requirement
# Create requirement detail
class ViewsParticipantValidity(TestCase):

    def setUp(self):
        populate_pf.populate()
        self.participant = Participant.objects.all()[0]

        # print self.participant
        self.experiment = Experiment.objects.get(name="It's all in the face!")
        # print experiment.name
        self.requirement = Requirement.objects.get(experiment=self.experiment)
        # print requirement
        self.requirement_detail = MatchingDetail.objects.get(requirement=self.requirement)
        # print requirement_detail

        # set all requirements to false
        self.requirement.student=False
        self.requirement.age = False
        self.requirement.language = False
        self.requirement.height = False
        self.requirement.weight = False
        self.requirement.gender = False
        self.requirement.save()
        refresh_reqs(self.experiment)
        # self.participant.userprofile.user.is_authenticated()

    def test_valid_student(self):
        # set requirement to require student participants
        self.requirement.student = True
        self.requirement.save()

        # Set participant as student
        self.participant.student = True
        self.participant.save()

        # Test to make sure valid student is eligible
        self.assertTrue(check_applicant_validity(self.participant.userprofile, self.experiment))

        # Test to make sure non-student is not eligible
        # Set participant.student to False
        self.participant.student = False
        self.participant.save()
        self.assertFalse(check_applicant_validity(self.participant.userprofile, self.experiment))
        # # exception should be raised
        # self.assertTrue(check_applicant_validity(self.participant.userprofile, self.experiment))

    def test_gender_male(self):
        # set gender requirement to true
        self.requirement.gender = True
        self.requirement.save()
        # Set required gender to female
        self.requirement_detail.gender = "Male"
        self.requirement_detail.save()

        # set participant gender to male
        self.participant.gender = "Male"
        self.participant.save()

        # Test to make sure male participant is eligible
        self.assertTrue(check_applicant_validity(self.participant.userprofile, self.experiment))

        # set participant gender to female
        self.participant.gender = "Female"
        self.participant.save()

        # Test to make sure non male applicants are not eligible
        self.assertFalse(check_applicant_validity(self.participant.userprofile, self.experiment))

    def test_gender_female(self):
        # set gender requirement to true
        self.requirement.gender = True
        self.requirement.save()
        # Set required gender to female
        self.requirement_detail.gender = "Female"
        self.requirement_detail.save()

        # set participant gender to female
        self.participant.gender = "Female"
        self.participant.save()

        # Test to make sure male participant is eligible
        self.assertTrue(check_applicant_validity(self.participant.userprofile, self.experiment))

        # set participant gender to male
        self.participant.gender = "Male"
        self.participant.save()

        # Test to make sure non male applicants are not eligible
        self.assertFalse(check_applicant_validity(self.participant.userprofile, self.experiment))

    def test_height(self):
        # Set height requirement to true
        self.requirement.height = True
        self.requirement.save()
        # Set height details
        self.requirement_detail.min_height = 100
        self.requirement_detail.max_height = 150
        self.requirement_detail.save()

        # Set participant height - 100cm
        self.participant.height = 100
        self.participant.save()

        # Test Min Height (equal to minimum accepted)
        self.assertTrue(check_applicant_validity(self.participant.userprofile, self.experiment))

        # Set participant height - 125cm
        self.participant.height = 125
        self.participant.save()

        # Test height in between min and max
        self.assertTrue(check_applicant_validity(self.participant.userprofile, self.experiment))

        # Set participant height to 150cm
        self.participant.height = 150
        self.participant.save()

        # Test max height (equal to max accepted)
        self.assertTrue(check_applicant_validity(self.participant.userprofile, self.experiment))

        # Test lower than min height
        self.participant.height = 80
        self.participant.save()
        self.assertFalse(check_applicant_validity(self.participant.userprofile, self.experiment))

        # Test higher that max height
        self.participant.height = 200
        self.participant.save()
        self.assertFalse(check_applicant_validity(self.participant.userprofile, self.experiment))

    def test_weight(self):
        # Set height requirement to true
        self.requirement.weight = True
        self.requirement.save()
        # Set weight details
        self.requirement_detail.min_weight = 60
        self.requirement_detail.max_weight = 65
        self.requirement_detail.save()

        # Set participant weight - 60kg
        self.participant.weight = 60
        self.participant.save()

        # Test Min Weight (equal to minimum accepted)
        self.assertTrue(check_applicant_validity(self.participant.userprofile, self.experiment))

        # Set participant weight - 61
        self.participant.weight = 61
        self.participant.save()

        # Test wweight in between min and max
        self.assertTrue(check_applicant_validity(self.participant.userprofile, self.experiment))

        # Set participant weight to 65
        self.participant.weight = 65
        self.participant.save()

        # Test max weight (equal to max accepted)
        self.assertTrue(check_applicant_validity(self.participant.userprofile, self.experiment))

        # Test lower than min weight
        self.participant.weight = 59
        self.participant.save()
        self.assertFalse(check_applicant_validity(self.participant.userprofile, self.experiment))

        # Test higher that max weight
        self.participant.weight = 66
        self.participant.save()
        self.assertFalse(check_applicant_validity(self.participant.userprofile, self.experiment))

    def test_language(self):
        # Set language requirement to true
        self.requirement.language = True
        self.requirement.save()

        # Set required languages(french and spanish)
        self.requirement_detail.l = "French, Spanish"
        self.requirement_detail.save()

        # Test for when participant doesn't have all of the required languages
        self.assertFalse(check_applicant_validity(self.participant.userprofile, self.experiment))

        # Make sure student has the required languages
        french = Languages.objects.get(language="French")
        spanish = Languages.objects.get(language="Spanish")
        self.participant.language.add(french)
        self.participant.language.add(spanish)
        self.participant.save()

        # Test for required languages
        self.assertTrue(check_applicant_validity(self.participant.userprofile, self.experiment))

    def test_age(self):
        # Set age requirement to true
        self.requirement.age = True
        self.requirement.save()

        # Set requirement detail
        self.requirement_detail.min_age = 18
        self.requirement_detail.max_age = 26
        self.requirement_detail.save()

        # Set participant age to meet requirements
        self.participant.dob = datetime.date(year=1990, month=10, day=10)
        self.participant.save()

        # test
        self.assertTrue(check_applicant_validity(self.participant.userprofile, self.experiment))
        # self.assertFalse(check_applicant_validity(self.participant.userprofile, self.experiment))

    def test_student_gender_age(self):
        # Test Combinations of requirements
        # Student, Gender, Age

        # set student, gender and age requirements to true
        self.requirement.student = True
        self.requirement.age = True
        self.requirement.gender = True
        self.requirement.save()

        # set requirement details
        # Age
        self.requirement_detail.min_age = 18
        self.requirement_detail.max_age = 25
        # Gender
        self.requirement_detail.gender = 'Male'
        self.requirement_detail.save()

        # Update participant details to meet requirements
        self.participant.dob = datetime.date(year=1992, month=10, day=10)
        self.participant.gender = 'Male'
        self.participant.student = True
        self.participant.save()
        # Test for student meeting all three requirements
        self.assertTrue(check_applicant_validity(self.participant.userprofile, self.experiment))

        # Test for student only meeting 2/3 requirements
        self.participant.dob = datetime.date(year=1980, month=10, day=10)
        self.participant.save()

        # Test for student being too old
        self.assertFalse(check_applicant_validity(self.participant.userprofile, self.experiment))

    # Test combination of requirements:
    # height, weight and language
    def test_height_weight_lang(self):
        # Set height, weight and language requirements to true
        self.requirement.height = True
        self.requirement.weight = True
        self.requirement.language = True
        self.requirement.save()

        # set requirement details
        # Weight
        self.requirement_detail.min_weight = 50
        self.requirement_detail.max_weight = 60

        # Height
        self.requirement_detail.min_height = 120
        self.requirement_detail.max_height = 150

        # Language
        self.requirement_detail.l = "German, Spanish"

        self.requirement_detail.save()

        # Update Participant details to meet requirements
        self.participant.height = 150
        self.participant.weight = 50

        # Get Spanish lang
        spanish = Languages.objects.get(language="Spanish")
        german = Languages.objects.get(language="German")
        self.participant.language.add(spanish)
        self.participant.language.add(german)
        print self.participant.language
        self.participant.save()

        # Test for student meeting all three requirements
        self.assertTrue(check_applicant_validity(self.participant.userprofile, self.experiment))

        # Test for missing one language, assertFalse
        self.participant.language.remove(german)
        self.participant.save()
        self.assertFalse(check_applicant_validity(self.participant.userprofile, self.experiment))


# Test individual matching tests in views_search
class ViewsIndividualSearch(TestCase):

    def setUp(self):
        populate_pf.populate()
        self.participant = Participant.objects.all()[0]

        # print self.participant
        self.experiment = Experiment.objects.get(name="It's all in the face!")
        # print experiment.name
        self.requirement = Requirement.objects.get(experiment=self.experiment)
        # print requirement
        self.requirement_detail = MatchingDetail.objects.get(requirement=self.requirement)
        # print requirement_detail

    def test_match_gender(self):
        # Set up gender requirement details
        self.requirement_detail.gender = "Female"
        self.requirement_detail.save()

        # Set up participant
        self.participant.gender = "Female"
        self.participant.save()

        # Test - assertTrue
        self.assertTrue(match_gender(self.participant, self.requirement_detail))

        # Test if gender does not meet requirement
        self.requirement_detail.gender = "Male"
        self.requirement_detail.save()
        # Test - assertFalse
        self.assertFalse(match_gender(self.participant, self.requirement_detail))

    def test_match_age(self):
        # Set up age detail requirement
        self.requirement_detail.min_age = 18
        self.requirement_detail.max_age = 25
        self.requirement_detail.save()

        # Set up participant details
        self.participant.dob = datetime.date(year=1992, month=10, day=10)
        self.participant.save()

        # Test - assertTrue
        self.assertTrue(match_age(self.participant, self.requirement_detail))

    def test_match_height(self):
        # Set up height detail requirements
        self.requirement_detail.min_height = 125
        self.requirement_detail.max_height = 150
        self.requirement_detail.save()

        # Set up participant details
        self.participant.height = 150
        self.participant.save()

        # Test - assertTrue
        self.assertTrue(match_height(self.participant, self.requirement_detail))

        # Test - assertFalse - too tall
        self.participant.height = 155
        self.participant.save()
        self.assertFalse(match_height(self.participant, self.requirement_detail))

    def test_match_weight(self):
        # Set up weight detail requirements
        self.requirement_detail.min_weight = 70
        self.requirement_detail.max_weight = 70
        self.requirement_detail.save()

        # Set up participant details
        self.participant.weight = 70
        self.participant.save()

        # Test - assertTrue
        self.assertTrue(match_weight(self.participant, self.requirement_detail))

        # Test - assertFalse - too heavy
        self.participant.weight = 100
        self.participant.save()
        self.assertFalse(match_weight(self.participant, self.requirement_detail))


# Tests for all models
class ModelTests(TestCase):

    # Setup Timeslot, Experiment and Researcher
    def setUp(self):
        populate_pf.populate()

        # user
        self.user = User.objects.get(username="fsmith")

        # User profile
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