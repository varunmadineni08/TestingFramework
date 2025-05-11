from pages.Basepage import BasePage


class AccountPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    validation_xpath = '//div[@id="content"]/h2[1]'


    def verify_logged_in(self):
        return self.check_display_status_of_element("validation_xpath",self.validation_xpath)

