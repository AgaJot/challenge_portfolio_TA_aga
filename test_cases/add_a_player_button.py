import os
import time
import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.add_a_player_form import AddaPlayerPage
from test_cases.login_to_the_system import TestLoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT



class TestAddaPlayerButton(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        super(TestAddaPlayerButton, self).setUp(self)

    def test_click_in_to_the_add_player_form(self):
        dashboard_page = Dashboard(self.driver)
        TestLoginPage.test_log_in_to_the_system(self)
        dashboard_page.click_on_the_add_player_button()
        add_a_player_form_page = AddaPlayerPage(self.driver)
        add_a_player_form_page.title_of_page()


    @classmethod
    def tearDown(self):
        self.driver.quit()