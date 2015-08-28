# from django.test import TestCase
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pf.settings")
# __author__ = 'patrickfrempong'
# from django.test import LiveServerTestCase
# from django.contrib.auth.models import User
#
# from selenium import webdriver
#
#
# class AdminTestCase(LiveServerTestCase):
#     def setUp(self):
#         # setUp is where you instantiate the selenium webdriver and loads the browser.
#         User.objects.create_superuser(
#             username='admin',
#             password='admin',
#             email='admin@examplex.com',
#             first_name='John',
#             last_name='Smith'
#         )
#
#         self.selenium = webdriver.Firefox()
#         self.selenium.maximize_window()
#         super(AdminTestCase, self).setUp()
#
#     def tearDown(self):
#         # Call tearDown to close the web browser
#         self.selenium.quit()
#         super(AdminTestCase, self).tearDown()
#
#     def test_create_user(self):
#         """
#         Django admin create user test
#         This test will create a user in django admin and assert that
#         page is redirected to the new user change form.
#         """
#         # Open the django admin page.
#         # DjangoLiveServerTestCase provides a live server url attribute
#         # to access the base url in tests
#         self.selenium.get(
#             '%s%s' % (self.live_server_url,  "/admin/")
#         )
#
#         # Fill login information of admin
#         username = self.selenium.find_element_by_id("id_username")
#         username.send_keys("admin")
#         password = self.selenium.find_element_by_id("id_password")
#         password.send_keys("admin")
#
#         # Locate Login button and click it
#         self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
#         self.selenium.get(
#             '%s%s' % (self.live_server_url, "/admin/auth/user/add/")
#         )
#
#         # Fill the create user form with username and password
#         self.selenium.find_element_by_id("id_username").send_keys("test")
#         self.selenium.find_element_by_id("id_password1").send_keys("test")
#         self.selenium.find_element_by_id("id_password2").send_keys("test")
#
#         # Forms can be submitted directly by calling its method submit
#         self.selenium.find_element_by_id("user_form").submit()
#         self.assertIn("Change user", self.selenium.title)

# from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.contrib.auth.models import User
import populate_pf
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
#
# driver = webdriver.Firefox()
# driver.implicitly_wait(10) # seconds

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
        self.selenium.find_element_by_link_text("Log out").click()


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
        university_select = self.selenium.find_element_by_xpath('//select[@id="id_university"]/option[@value="9"]').click()
        course_name_input = self.selenium.find_element_by_id('id_course_name')
        course_name_input.send_keys('MSc Information Technology')
        yos_select = self.selenium.find_element_by_xpath('//select[@id="id_year_of_study"]/option[@value="2"]').click()
        matric_input = self.selenium.find_element_by_id('id_matric')
        matric_input.send_keys('25241254125')
        gender_select = self.selenium.find_element_by_xpath('//select[@id="id_gender"]/option[@value="Male"]').click()
        height_input = self.selenium.find_element_by_id('id_height')
        height_input.send_keys('150')
        weight_input = self.selenium.find_element_by_id('id_eeight')
        weight_input.send_keys('70')
        part_2_submit = self.selenium.find_element_by_class_name("btn-default").click()













