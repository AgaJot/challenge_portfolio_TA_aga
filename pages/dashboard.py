import time

from pages.base_page import BasePage


class Dashboard(BasePage):
strona_główna_button_xpath = "//*[text()='Strona główna']"
dev_team_contact_hyperlink_xpath = "//a[starts-with(@href,'https')]"
dodaj_gracza_button_xpath = "//a[contains(@href, '/pl/players/add')]"
english_button_xpath = "//*[text()='English']"
wyloguj_button_xpath = "//*[text()='Wyloguj']"
logo_xpath = "//*[contains(@title, 'Logo')]"
scouts_panel_upper_xpath = "//h6[text()='Scouts Panel']"
scouts_panel_bottom_xpath = "//h2[text()='Scouts Panel']"
ilość_raportów_xpath = "//*[text()='Ilość raportów']"
wróć_do_raportu_buttons_xpath = "//*[text()='Wróć do raportu']"
pass
    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'
    add_player_button_xpath = "//*[text()='Add player']"
    futbol_kolektyw_logo_xpath = "//*[@title='Logo Scouts Panel']"
    wait = WebDriverWait(driver, 10)

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.futbol_kolektyw_logo_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)
