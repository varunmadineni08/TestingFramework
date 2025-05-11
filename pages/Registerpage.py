from pages.AccountSuccesspage import AccountSuccessPage
from pages.Basepage import BasePage


class RegisterPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    firstname_id="input-firstname"
    lastname_id="input-lastname"
    email_id="input-email"
    telephone_id="input-telephone"
    password_id="input-password"
    confirm_password_id="input-confirm"
    radio_button_xpath='//label[text()="Yes"]'
    checkbox_xpath="//input[@type='checkbox']"
    submit_xpath='//input[@type="submit"]'

    existing_mail_warning_xpath='//div[contains(text(),"Warning: E-Mail Address is already registered!")]'
    
    privacy_warning_xpath='//ul[@class="breadcrumb"]/following-sibling::div[1]'
    first_name_warning_xpath='//input[@id="input-firstname"]/following-sibling::div'
    last_name_warning_xpath='//input[@id="input-lastname"]/following-sibling::div'
    email_empty_warning_xpath='//input[@id="input-email"]/following-sibling::div'
    telephone_warning_xpath='//input[@id="input-telephone"]/following-sibling::div'
    password_warning_xpath='//input[@id="input-password"]/following-sibling::div'

    def enter_firstname(self,firstname):
        self.enter_text(firstname,"firstname_id",self.firstname_id)

    def enter_lastname(self,lastname):
        self.enter_text(lastname,"lastname_id",self.lastname_id)

    def enter_email(self,email):
        self.enter_text(email,"email_id",self.email_id)

    def enter_telephone(self,telephone):
        self.enter_text(telephone,"telephone_id",self.telephone_id)

    def enter_password(self,password):
        self.enter_text(password,"password_id",self.password_id)

    def enter_confirm_password(self,confirm_password):
        self.enter_text(confirm_password,"confirm_password_id",self.confirm_password_id)

    def click_radio_button(self):
        self.click_element("radio_button_xpath",self.radio_button_xpath)

    def click_check_box(self):
        self.click_element("checkbox_xpath",self.checkbox_xpath)

    def click_submit(self):
        self.click_element("submit_xpath",self.submit_xpath)

        return AccountSuccessPage(self.driver)

    #existing warning
    def email_warning(self):
        return self.check_display_status_of_element("existing_mail_warning_xpath",self.existing_mail_warning_xpath)


    #emptywarning
    def empty_privacy_warning(self):
        return self.check_display_status_of_element("privacy_warning_xpath",self.privacy_warning_xpath)

    def empty_firstname_warning(self):
        return self.check_display_status_of_element("first_name_warning_xpath",self.first_name_warning_xpath)

    def empty_lastname_warning(self):
        return self.check_display_status_of_element("last_name_warning_xpath",self.last_name_warning_xpath)

    def empty_email_warning(self):
        return self.check_display_status_of_element("email_empty_warning_xpath",self.email_empty_warning_xpath)

    def empty_telephone_warning(self):
        return self.check_display_status_of_element("telephone_warning_xpath",self.telephone_warning_xpath)

    def empty_password_warning(self):
        return self.check_display_status_of_element("password_warning_xpath",self.password_warning_xpath)

    ########optimization
    def enter_registering_details(self,firstname,lastname,email,telephone,password,confirm_password,yes_or_no,privacy_button):
        self.enter_firstname(firstname)
        self.enter_lastname(lastname)
        self.enter_email(email)
        self.enter_telephone(telephone)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)
        if yes_or_no=="Yes":
            self.click_radio_button()
        if privacy_button=="select":
            self.click_check_box()
        return self.click_submit()

    def warnings(self):
        return(self.empty_privacy_warning() and
        self.empty_firstname_warning() and
        self.empty_lastname_warning() and
        self.empty_email_warning() and
        self.empty_telephone_warning() and
        self.empty_password_warning())










