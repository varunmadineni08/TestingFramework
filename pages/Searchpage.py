from pages.Basepage import BasePage

class SearchPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    product_link_text="HP LP3065"
    product_validation_xpath="//p[contains(text(),'There is no product')]"


    def search_for_valid_product(self):
        return self.check_display_status_of_element("product_link_text",self.product_link_text)

    def search_for_product(self):
        return self.check_display_status_of_element("product_validation_xpath",self.product_validation_xpath)





