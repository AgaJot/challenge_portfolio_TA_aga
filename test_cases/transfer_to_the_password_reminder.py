import os
import time
import unittest
from selenium import webdriver

from pages.password_reminder import PasswordReminderPage
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT



class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_transfer_to_the_password_reminder(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.click_on_the_remind_password_hyperlink()
        password_reminder_page = PasswordReminderPage(self.driver)
        password_reminder_page.title_of_page()

    @classmethod
    def tearDown(self):
        self.driver.quit()