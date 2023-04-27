from pages.base_page import BasePage


class AddaMatch(BasePage):
    my_team_field_xpath = "//input[@name='myTeam']"
    my_team_title_xpath = "//*[text()='My team']"
    required_information_xpath = "//*[text()='Required']"
    date_field_xpath = "//input[@name='date']"
    clear_button_xpath = "//button[contains(@class,'MuiButton-containedSecondary')]"
    match_out_home_xpath = "//*[text()='Match out home']"
    adding_match_player_xpath = "//span[contains(@class, 'title')]"
    matches_button_xpath = "//*[text()='Matches']"
    time_played_field_xpath = "//input[@name='timePlayed']"
    number_field_xpath = "//input[@name='number']"

pass