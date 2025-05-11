from pages.Basepage import BasePage
from pages.Loginpage import LoginPage
from pages.Registerpage import RegisterPage
from pages.Searchpage import SearchPage


class HomePage(BasePage):
    def __init__(self,driver):
       super().__init__(driver)

    search_input_box_name="search"
    search_button_class="input-group-btn"

    my_account_button_class='caret'
    login_button_xpath='//ul/descendant::a[text()="Login"]'
    register_button_link_text="Register"


    def enter_product_search_box(self,product_name):
        self.enter_text(product_name,"search_input_box_name",self.search_input_box_name)

    def click_search_button(self):
        self.click_element("search_button_class",self.search_button_class)
        return SearchPage(self.driver)

    def click_on_my_account(self):
        self.click_element("my_account_button_class",self.my_account_button_class)

    def click_on_login_button(self):
        self.click_element("login_button_xpath",self.login_button_xpath)
        return LoginPage(self.driver)

    def click_on_register(self):
        self.click_element("register_button_link_text",self.register_button_link_text)
        return RegisterPage(self.driver)

    def search_for_a_valid_product(self,product_name):
        self.enter_product_search_box(product_name)
        return self.click_search_button()

    def go_to_login_page(self):
        self.click_on_my_account()
        return self.click_on_login_button()

    def got_to_register(self):
        self.click_on_my_account()
        return self.click_on_register()



