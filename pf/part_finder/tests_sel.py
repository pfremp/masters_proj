__author__ = 'patrickfrempong'
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





class MySeleniumTests(StaticLiveServerTestCase):
    fixtures = ['user-data.json']




    @classmethod
    def setUpClass(cls):

        User.objects.create_superuser(
            username='pf',
            password='1',
            email='admin@examplex.com',
            first_name='John',
            last_name='Smith'
        )


        super(MySeleniumTests, cls).setUpClass()
        cls.selenium = WebDriver()



    # @classmethod
    # def tearDownClass(cls):
    #     cls.selenium.quit()
    #     super(MySeleniumTests, cls).tearDownClass()

    def test_login(self):
        populate_pf.populate()
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('pf')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('1')
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
        # self.selenium.find_element_by_link_text("Log out").click()
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/logout/'))


    def test_participant_login(self):
        populate_pf.populate()
        self.selenium.get('%s%s' % (self.live_server_url, '/part_finder/'))
        login_page = self.selenium.find_element_by_link_text("Login").click()
        username_input = self.selenium.find_element_by_id("id_login")
        username_input.send_keys("andrews1")
        password_input = self.selenium.find_element_by_id("id_password")
        password_input.send_keys("111111")
        login_submit = self.selenium.find_element_by_class_name("btn-default").click()
        # self.selenium.get('%s%s' % (self.live_server_url, '/part_finder/my_experiments'))

    def test_participant_signup(self):
        populate_pf.populate()
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/signup/'))
        first_name_input = self.selenium.find_element_by_id('id_first_name')
        first_name_input.send_keys("Patrick")
        last_name_input = self.selenium.find_element_by_id('id_last_name')
        last_name_input.send_keys("Frempong")
        account_type = self.selenium.find_element_by_id('id_type_0').click()
        username_input = self.selenium.find_element_by_id('id_username')
        username_input.send_keys('pfremp1')
        email_input = self.selenium.find_element_by_id('id_email')
        email_input.send_keys('p-fremp@hotmail.com')
        password_input_1 = self.selenium.find_element_by_id('id_password1')
        password_input_1.send_keys('111111')
        password_input_2 = self.selenium.find_element_by_id('id_password2')
        password_input_2.send_keys('111111')
        signup_submit = self.selenium.find_element_by_class_name("btn-default").click()

        # Participant Form 1
        contact_number_input = self.selenium.find_element_by_id('id_contact_number')
        contact_number_input.send_keys('01415558585')
        student_input = self.selenium.find_element_by_id('id_student').click()
        part_1_submit = self.selenium.find_element_by_class_name("btn-default").click()

        # Participant Form 2
        education_select = self.selenium.find_element_by_xpath('//select[@id="id_education"]/option[@value="HE3"]').click()
        university_select = self.selenium.find_element_by_xpath('//select[@id="id_university"]/option[2]').click()
        course_name_input = self.selenium.find_element_by_id('id_course_name')
        course_name_input.send_keys('MSc Information Technology')
        yos_select = self.selenium.find_element_by_xpath('//select[@id="id_year_of_study"]/option[@value="2"]').click()
        matric_input = self.selenium.find_element_by_id('id_matric')
        matric_input.send_keys('25241254125')
        gender_select = self.selenium.find_element_by_xpath('//select[@id="id_gender"]/option[@value="Male"]').click()
        height_input = self.selenium.find_element_by_id('id_height')
        height_input.send_keys('150')
        weight_input = self.selenium.find_element_by_id('id_weight')
        weight_input.send_keys('70')
        part_2_submit = self.selenium.find_element_by_class_name("btn-default").click()



    def test_experiment_signup(self):
        populate_pf.populate()
        self.selenium.get('%s%s' % (self.live_server_url, '/part_finder/'))
        login_page = self.selenium.find_element_by_link_text("Login").click()
        username_input = self.selenium.find_element_by_id("id_login")
        username_input.send_keys("andrews1")
        password_input = self.selenium.find_element_by_id("id_password")
        password_input.send_keys("111111")
        login_submit = self.selenium.find_element_by_class_name("btn-default").click()
        select_experiment = self.selenium.find_elements_by_class_name('btn-primary')
        select_experiment[0].click()
        timeslot_select = self.selenium.find_element_by_xpath('//select[@id="id_timeslot"]/option[2]').click()
        apply_select = self.selenium.find_element_by_class_name("btn-default").click()

    def test_res_reg(self):
        populate_pf.populate()
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/signup/'))
        first_name_input = self.selenium.find_element_by_id('id_first_name')
        first_name_input.send_keys("Patrick")
        last_name_input = self.selenium.find_element_by_id('id_last_name')
        last_name_input.send_keys("Frempong")
        account_type = self.selenium.find_element_by_id('id_type_1').click()
        username_input = self.selenium.find_element_by_id('id_username')
        username_input.send_keys('drfremp')
        email_input = self.selenium.find_element_by_id('id_email')
        email_input.send_keys('p-fremp@hotmail.com')
        password_input_1 = self.selenium.find_element_by_id('id_password1')
        password_input_1.send_keys('111111')
        password_input_2 = self.selenium.find_element_by_id('id_password2')
        password_input_2.send_keys('111111')
        signup_submit = self.selenium.find_element_by_class_name("btn-default").click()

        # Researcher Signup
        university_select = self.selenium.find_element_by_xpath('//select[@id="id_university"]/option[2]').click()
        dept_name_input = self.selenium.find_element_by_id('id_department')
        dept_name_input.send_keys('Computing')
        contact_no_input = self.selenium.find_element_by_id('id_contact_no')
        contact_no_input.send_keys('01412563256')
        url_input = self.selenium.find_element_by_id('id_url')
        url_input.send_keys('http://google.com')
        researcher_details = self.selenium.find_element_by_class_name("btn-default").click()


    def add_exp(self):
        populate_pf.populate()

        # Login
        self.selenium.get('%s%s' % (self.live_server_url, '/part_finder/'))
        login_page = self.selenium.find_element_by_link_text("Login").click()
        username_input = self.selenium.find_element_by_id("id_login")
        username_input.send_keys("fsmith")
        password_input = self.selenium.find_element_by_id("id_password")
        password_input.send_keys("111111")
        login_submit = self.selenium.find_element_by_class_name("btn-default").click()

        # Add Experiment
        self.selenium.get('%s%s' % (self.live_server_url, '/part_finder/add_experiment/'))
        exp_name_input = self.selenium.find_element_by_id("id_name")
        exp_name_input.send_keys("Science Experiment")
        desc_input = self.selenium.find_element_by_id("id_long_description")
        desc_input.send_keys("Science Experiment Description")
        duration_input = self.selenium.find_element_by_id("id_duration")
        duration_input.send_keys("60")
        address_input = self.selenium.find_element_by_id("id_address")
        address_input.send_keys("George St, Glasgow, G2 1DU")
        url_input = self.selenium.find_element_by_id("id_url")
        url_input.send_keys("google.com")

        # Payment Details
        is_paid = self.selenium.find_element_by_xpath('//select[@id="id_is_paid"]/option[2]').click()
        currency = self.selenium.find_element_by_xpath('//select[@id="id_currency"]/option[2]').click()
        currency = self.selenium.find_element_by_xpath('//select[@id="id_payment_type"]/option[2]').click()
        payment_input = self.selenium.find_element_by_id("id_amount")
        payment_input.send_keys("8")

        # Requirements
        student = self.selenium.find_element_by_xpath('//select[@id="id_student"]/option[3]').click()
        age = self.selenium.find_element_by_xpath('//select[@id="id_age"]/option[2]').click()
        lang = self.selenium.find_element_by_xpath('//select[@id="id_language"]/option[2]').click()
        height = self.selenium.find_element_by_xpath('//select[@id="id_height"]/option[2]').click()
        weight = self.selenium.find_element_by_xpath('//select[@id="id_weight"]/option[2]').click()
        gender = self.selenium.find_element_by_xpath('//select[@id="id_gender"]/option[2]').click()

        # Timeslot 1

        # Old Date Format
        # ts1_date_input = self.selenium.find_element_by_id("id_form-0-date")
        # ts1_date_input.send_keys("30/10/2015")

        # New date format
        ts1_day_input = self.selenium.find_element_by_xpath('//select[@id="id_form-0-date_day"]/option[2]').click()
        ts1_month_input = self.selenium.find_element_by_xpath('//select[@id="id_form-0-date_month"]/option[3]').click()
        ts1_year_input = self.selenium.find_element_by_xpath('//select[@id="id_form-0-date_year"]/option[3]').click()

        ts1_stime_input = self.selenium.find_element_by_id("id_form-0-start_time")
        ts1_stime_input.send_keys("12:00")
        ts1_etime_input = self.selenium.find_element_by_id("id_form-0-end_time")
        ts1_etime_input.send_keys("13:00")
        ts1_np_input = self.selenium.find_element_by_id("id_form-0-no_of_parts")
        ts1_np_input.send_keys("2")

        # #add new timeslot
        # # add_ts2 = self.selenium.find_element_by_xpath('//select[@id="add"]').click()
        # add_ts2 = self.selenium.find_element_by_id("add").click()
        #
        # wait = WebDriverWait(self.selenium, 10)
        # element = wait.until(EC.element_to_be_clickable((By.ID,'someid')))
        #
        # # Timeslot 2
        # ts2_date_input = self.selenium.find_element_by_id("id_form-1-date")
        # ts2_date_input.send_keys("10/11/2015")
        # ts2_stime_input = self.selenium.find_element_by_id("id_form-1-start_time")
        # ts2_stime_input.send_keys("14:00")
        # ts2_etime_input = self.selenium.find_element_by_id("id_form-1-end_time")
        # ts2_etime_input.send_keys("15:00")
        # ts2_np_input = self.selenium.find_element_by_id("id_form-1-no_of_parts").clear()
        # ts2_np_input.send_keys("3")
        exp_submit = self.selenium.find_element_by_class_name("btn-default").click()



