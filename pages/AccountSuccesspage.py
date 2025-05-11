from pages.Basepage import BasePage


class AccountSuccessPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
    account_register_xpath = '//div/h1[contains(text(),"Your Account Has Been Created!")]'

    def register_success(self):
        return self.check_display_status_of_element("account_register_xpath",self.account_register_xpath)