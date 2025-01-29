import time
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client
from base.models import Task


class TestTaskListPage(StaticLiveServerTestCase):
    def setUp(self) -> None:
        # self.browser = webdriver.Chrome('base/tests/functional_tests/chromedriver.exe')
        self.browser = webdriver.Chrome()
        self.url = self.live_server_url

    def tearDown(self) -> None:
        self.browser.close()

    def test_homepage(self):
        '''
        Get Test of HomePage(Login)
        '''
        login_url = self.url + reverse('login') + '?next=/'
        self.browser.get(self.url)
        self.assertEqual(self.browser.current_url, login_url)

    def test_register_button_redirection(self):
        '''
        This Test Ensures that Register button redirects us to register page
        '''
        register_url = self.url + reverse('register')
        self.browser.get(self.url)
        register_btn = self.browser.find_element(By.CLASS_NAME, 'register-btn')
        register_btn.click()
        self.assertEqual(self.browser.current_url, register_url)

    def test_user_register(self):
        name = 'random'
        password = 'User123register'
        self.browser.get(self.url)
        self.browser.find_element(By.CLASS_NAME, 'register-btn').click()

        username_box = self.browser.find_element(By.ID, 'id_username')
        username_box.click()
        username_box.send_keys(name)

        password1_box = self.browser.find_element(By.ID, 'id_password1')
        password1_box.click()
        password1_box.send_keys(password)

        password2_box = self.browser.find_element(By.ID, 'id_password2')
        password2_box.click()
        password2_box.send_keys(password)

        self.browser.find_element(By.CSS_SELECTOR, 'body > div > form > button').click()

        time.sleep(1)
        self.assertEqual(self.browser.current_url, self.url+'/')

        elem = self.browser.find_element(By.CSS_SELECTOR, 'body > div > h3:nth-child(8)')
        self.assertEqual(elem.text, name)

    def test_user_login(self):
        name = 'login_user'
        password = 'User123login'
        test_user = User.objects.create_user(username=name, password=password)

        self.browser.get(self.url)

        username_box = self.browser.find_element(By.ID, 'id_username')
        username_box.click()
        username_box.send_keys(name)

        password_box = self.browser.find_element(By.ID, 'id_password')
        password_box.click()
        password_box.send_keys(password)

        self.browser.find_element(By.CSS_SELECTOR, 'body > div > form > button').click()
        time.sleep(2)

        self.assertEqual(self.browser.current_url, self.url + '/')

        elem = self.browser.find_element(By.CSS_SELECTOR, 'body > div > h3:nth-child(8)')
        self.assertEqual(elem.text, name)

    def test_user_login_and_task_creation(self):
        name = 'already_logined_user'
        password = 'User12345login'
        test_user = User.objects.create_user(username=name, password=password)

        self.browser.get(self.url)

        username_box = self.browser.find_element(By.ID, 'id_username')
        username_box.click()
        username_box.send_keys(name)

        password_box = self.browser.find_element(By.ID, 'id_password')
        password_box.click()
        password_box.send_keys(password)

        self.browser.find_element(By.CSS_SELECTOR, 'body > div > form > button').click()
        time.sleep(2)

        self.browser.find_element(By.CSS_SELECTOR, 'body > div > h3:nth-child(13) > a').click()
        time.sleep(1)

        title_box = self.browser.find_element(By.ID, 'id_title')
        title_box.click()
        title_box.send_keys('Selenium Task')

        self.browser.find_element(By.CSS_SELECTOR, 'body > div > form > button').click()
        time.sleep(1)

        elem = self.browser.find_element(By.ID, 'completed-count')
        self.assertEqual(elem.text, 'Not Completed Tasks: 1')





