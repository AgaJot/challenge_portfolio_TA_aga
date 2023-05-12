from pages.base_page import BasePage


class PasswordReminderPage(BasePage):
    add_player_url = 'https://scouts.futbolkolektyw.pl/en/remind'
    expected_title = "Remind password"
    email_field_xpath = "//input[@name='email']"

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.email_field_xpath)
        assert self.get_page_title(self.add_player_url) == self.expected_title

