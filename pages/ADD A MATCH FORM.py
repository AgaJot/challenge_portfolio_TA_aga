from pages.base_page import BasePage


class Dashboard(BasePage):
    my_team_field_xpath = "//input[@name='myTeam']"
    my_team_title_xpath = "//*[text()='My team']"
    required_information_xpath = "//*[text()='Required']"
    date_field_xpath = "//input[@name='date']"
    clear_button_xpath = "//*[text()='Clear']"
    match_out_home_xpath = "//*[text()='Match out home']"
    adding_match_player_xpath = "//span[contains(@class, 'title')]"
    matches_button_xpath = "//*[text()='Matches']"
    edit_button_xpath = "//button[@title='Edit']"
    start_report_button_xpath = "//button[@title='Start report']"

pass