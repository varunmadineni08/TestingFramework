import time
from datetime import datetime

from pages.Homepage import HomePage
from pages.Loginpage import LoginPage
from tests.Basetest import BaseTest


class TestLogin(BaseTest):
    def test_login_valid_credentials(self):
        home_page=HomePage(self.driver)
        login_page=home_page.go_to_login_page()
        account_page=login_page.enter_login_details("varunmadineni@gmail.com","12345")
        assert account_page.verify_logged_in()

    def test_login_with_invalid_mail_and_valid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.go_to_login_page()
        login_page.enter_login_details( self.generate_mail_with_time_stamp(),"12345")
        time.sleep(3)
        assert login_page.invalid_mail_warning()


    def test_login_with_valid_mail_and_invalid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.go_to_login_page()
        login_page.enter_login_details("varunmadineni@gmail.com","1234567890")
        time.sleep(2)
        assert login_page.invalid_mail_warning()


    def test_login_with_empty_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.go_to_login_page()
        login_page.enter_login_details("","")
        time.sleep(2)
        assert login_page.invalid_mail_warning()


    def generate_mail_with_time_stamp(self):
        time_stamp=datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return f"varunmadineni{time_stamp}@gmail.com"


