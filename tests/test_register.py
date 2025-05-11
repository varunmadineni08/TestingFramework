from datetime import datetime
from pages.Homepage import HomePage
from tests.Basetest import BaseTest


class TestRegister(BaseTest):
    def test_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        register_page=home_page.got_to_register()
        account_success_page=register_page.enter_registering_details("varun","madineni",self.generate_email(),"1234567890","12345","12345","no","select")
        assert account_success_page.register_success()

    def test_with_all_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.got_to_register()
        account_success_page = register_page.enter_registering_details("varun", "madineni", self.generate_email(),
                                                                       "1234567890", "12345", "12345", "Yes", "select")
        assert account_success_page.register_success()

    def test_with_existing_mail(self):
        home_page = HomePage(self.driver)
        register_page = home_page.got_to_register()
        register_page.enter_registering_details("varun", "madineni", "varunmadineni@gmail.com",
                                                                       "1234567890", "12345", "12345", "Yes", "select")
        assert register_page.email_warning()

    def test_with_empty_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.got_to_register()
        register_page.enter_registering_details("","","","", "", "", "", "")
        assert register_page.warnings()

    def generate_email(self):
        time_stamp=datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return f"varun{time_stamp}@gmail.com"
