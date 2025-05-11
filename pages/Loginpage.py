from pages.Accountpage import AccountPage
from pages.Basepage import BasePage

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
    email_id = "input-email"
    password_id = "input-password"
    login_button_xpath = "//input[@value='Login']"
    invalid_mail_xpath = '//ul[@class="breadcrumb"]/following-sibling::div[1]'

    def enter_email(self, email):
        self.enter_text(email,"email_id",self.email_id)

    def enter_password(self, password):
        self.enter_text(password,"password_id",self.password_id)

    def click_login(self):
        self.click_element("login_button_xpath",self.login_button_xpath)
        return AccountPage(self.driver)

    def invalid_mail_warning(self):
        return self.check_display_status_of_element("invalid_mail_xpath",self.invalid_mail_xpath)

    def enter_login_details(self,email,password):
        self.enter_email(email)
        self.enter_password(password)
        return self.click_login()