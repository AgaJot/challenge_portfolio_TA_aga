import os
import time
import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.add_a_player_form import AddaPlayerPage
from test_cases.login_to_the_system import TestLoginPage
from test_cases.add_a_player_button import TestAddaPlayerButton
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT



class TestPlayerForm(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_youtube_link(self):
        add_a_player_form_page = AddaPlayerPage(self.driver)
        TestAddaPlayerButton.test_click_in_to_the_add_player_form(self)
        add_a_player_form_page.type_in_name('Piotr')
        add_a_player_form_page.type_in_surname('Kowalski')
        add_a_player_form_page.type_in_age('01101999')
        add_a_player_form_page.type_in_main_position('goalkeeper')
        add_a_player_form_page.click_on_the_add_link_to_youtube_button()
        add_a_player_form_page.type_in_youtube('https: // www.youtube.com / watch?v = MI_gFi_Zd8c')
        add_a_player_form_page.click_on_the_submit_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.find_last_created_player()


    @classmethod
    def tearDown(self):
        self.driver.quit()