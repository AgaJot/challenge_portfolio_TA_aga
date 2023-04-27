from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()='Sign in']"
    scouts_panel_xpath = "/html/body/div/form/div/div[1]/h5"
    login_url = ('https://scouts-test.futbolkolektyw.pl/en')
    expected_title = "Scouts panel - sign in"
    remind_password_hyperlink_xpath = "//*[text()='Remind password']"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def click_on_the_remind_password_hyperlink(self):
        self.click_on_the_element(self.remind_password_hyperlink_xpath)




