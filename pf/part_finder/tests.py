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
        # populate_pf.populate()

        super(MySeleniumTests, cls).setUpClass()
        cls.selenium = WebDriver()



    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(MySeleniumTests, cls).tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('pf')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('1')
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
        self.selenium.find_element_by_link_text("Log out").click()
        # self.selenium.implicitly_wait(10)
        # WebDriver.implicitly_wait(self.selenium,10)


    def test_participant_signup(self):
        populate_pf.populate()
        self.selenium.get('%s%s' % (self.live_server_url, '/part_finder/'))
        login_page = self.selenium.find_element_by_link_text("Login").click()
        username_input = self.selenium.find_element_by_id("id_login")
        username_input.send_keys("andrews1")
        password_input = self.selenium.find_element_by_id("id_password")
        password_input.send_keys("111111")
        login_submit = self.selenium.find_element_by_class_name("btn-default").click()
        self.selenium.implicitly_wait(10)
        self.selenium.get('%s%s' % (self.live_server_url, '/part_finder/my_experiments'))
        self.selenium.implicitly_wait(10)
