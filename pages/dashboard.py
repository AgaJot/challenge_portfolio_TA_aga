from pages.base_page import BasePage


class Dashboard(BasePage):
strona_główna_button_xpath = "//*[text()='Strona główna']"
dev_team_contact_button_xpath = "//a[starts-with(@href,'https')]"
dodaj_gracza_button_xpath = "//a[contains(@href, '/pl/players/add')]"
english_button_xpath = "//*[text()='English']"
wyloguj_button_xpath = "//*[text()='Wyloguj']"
logo_xpath = "//*[contains(@title, 'Logo')]"
scouts_panel_upper_xpath = "//h6"
scouts_panel_bottom_xpath = "//*[contains(@class, 'Bottom')]"
ilość_raportów_xpath = "//*[text()='Ilość raportów']"
niezapisany_mecz_xpath = "//*[text()='Niezapisany mecz']"
pass