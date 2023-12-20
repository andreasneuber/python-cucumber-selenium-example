from seleniumpagefactory.Pagefactory import PageFactory
from config.base import Config


class ProvideYourDetailsPage(PageFactory):
    """Described 'ProvideYourDetailsPage' page."""

    locators = {
        "input_fname": ('ID', 'fname'),
        "input_lname": ('ID', 'lname'),
        "input_street": ('ID', 'street'),
        "input_city": ('ID', 'city'),
        "input_zip": ('ID', 'zip'),
        "input_state": ('ID', 'state'),
        "input_country": ('ID', 'country'),
        "input_mobile": ('ID', 'mobile'),
        "input_home": ('ID', 'home'),
        "input_email": ('ID', 'email'),
        "btn_submit_info": ('ID', 'submit-info'),
    }

    def __init__(self, driver):
        super().__init__()
        self.url = Config.URL + '?action=form1'
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)

    def provide_first_name(self, first_name):
        self.input_fname.clear()
        self.input_fname.send_keys(first_name)

    def provide_last_name(self, last_name):
        self.input_lname.clear()
        self.input_lname.send_keys(last_name)

    def provide_street(self, street):
        self.input_street.clear()
        self.input_street.send_keys(street)

    def provide_city(self, city):
        self.input_city.clear()
        self.input_city.send_keys(city)

    def provide_zip(self, zip_code):
        self.input_zip.clear()
        self.input_zip.send_keys(zip_code)

    def provide_state(self, state):
        self.input_state.clear()
        self.input_state.send_keys(state)

    def provide_country(self, country):
        self.input_country.clear()
        self.input_country.send_keys(country)

    def provide_mobile_phone_number(self, number):
        self.input_mobile.clear()
        self.input_mobile.send_keys(number)

    def provide_home_phone_number(self, number):
        self.input_home.clear()
        self.input_home.send_keys(number)

    def provide_email(self, email):
        self.input_email.clear()
        self.input_email.send_keys(email)

    def click_submit_your_information(self):
        self.btn_submit_info.click()
