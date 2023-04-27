from lib2to3.pgen2 import driver

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class AddaPlayerPage(BasePage):
    add_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    expected_title = "Add player"
    name_field_xpath = "//input[@name='name']"
    surname_field_xpath = "//input[@name='surname']"
    age_field_xpath = "//input[@name='age']"
    main_position_field_xpath = "//input[@name='mainPosition']"
    submit_button_xpath = "//*[text()='Submit']"
    add_link_to_youtube_button_xpath = "//*[text()='Add link to Youtube']"
    youtube_field_xpath = "//input[@name='webYT[0]']"
    saved_player_alert_xpath = "//*[text()='Saved player.']"
    wait = WebDriverWait(driver, 15)

    def title_of_page(self):
        assert self.get_page_title(self.add_player_url) == self.expected_title

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_age(self, age):
        self.field_send_keys(self.age_field_xpath, age)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_field_xpath, main_position)

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def click_on_the_add_link_to_youtube_button(self):
        self.click_on_the_element(self.add_link_to_youtube_button_xpath)

    def type_in_youtube(self, youtube):
        self.field_send_keys(self.youtube_field_xpath, youtube)

    def wait_for_alert(self):
        self.wait_for_visibility_of_element_located(self.saved_player_alert_xpath)

