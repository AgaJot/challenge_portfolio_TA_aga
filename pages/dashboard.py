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