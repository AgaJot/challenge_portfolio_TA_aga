from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()='Sign in']"
    remind_password_button_xpath = "//*[text()='Remind password']"
    english_button_xpath = "//*[text()='English']"
    polski_button_xpath = "//*[text()='Polski']"
    scouts_panel_xpath = "/html/body/div/form/div/div[1]/h5"


    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
