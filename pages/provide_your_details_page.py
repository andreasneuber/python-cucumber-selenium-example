from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from config.base import Config


class ProvideYourDetailsPage:
    """Described 'ProvideYourDetailsPage' page."""

    INPUT_FNAME = (By.ID, "fname")
    INPUT_LNAME = (By.ID, "lname")
    INPUT_STREET = (By.ID, "street")
    INPUT_CITY = (By.ID, "city")
    INPUT_ZIP = (By.ID, "zip")
    INPUT_STATE = (By.ID, "state")
    INPUT_COUNTRY = (By.ID, "country")
    INPUT_MOBILE = (By.ID, "mobile")
    INPUT_HOME = (By.ID, "home")
    INPUT_EMAIL = (By.ID, "email")
    BTN_SUBMIT_INFO = (By.ID, "submit-info")

    def __init__(self, driver: Chrome):
        self.url = Config.URL + '?action=form1'
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)

    def provide_first_name(self, first_name):
        self.driver.find_element(*self.INPUT_FNAME).clear()
        self.driver.find_element(*self.INPUT_FNAME).send_keys(first_name)

    def provide_last_name(self, last_name):
        self.driver.find_element(*self.INPUT_LNAME).clear()
        self.driver.find_element(*self.INPUT_LNAME).send_keys(last_name)

    def provide_street(self, street):
        self.driver.find_element(*self.INPUT_STREET).clear()
        self.driver.find_element(*self.INPUT_STREET).send_keys(street)

    def provide_city(self, city):
        self.driver.find_element(*self.INPUT_CITY).clear()
        self.driver.find_element(*self.INPUT_CITY).send_keys(city)

    def provide_zip(self, zip_code):
        self.driver.find_element(*self.INPUT_ZIP).clear()
        self.driver.find_element(*self.INPUT_ZIP).send_keys(zip_code)

    def provide_state(self, state):
        self.driver.find_element(*self.INPUT_STATE).clear()
        self.driver.find_element(*self.INPUT_STATE).send_keys(state)

    def provide_country(self, country):
        self.driver.find_element(*self.INPUT_COUNTRY).clear()
        self.driver.find_element(*self.INPUT_COUNTRY).send_keys(country)

    def provide_mobile_phone_number(self, number):
        self.driver.find_element(*self.INPUT_MOBILE).clear()
        self.driver.find_element(*self.INPUT_MOBILE).send_keys(number)

    def provide_home_phone_number(self, number):
        self.driver.find_element(*self.INPUT_HOME).clear()
        self.driver.find_element(*self.INPUT_HOME).send_keys(number)

    def provide_email(self, email):
        self.driver.find_element(*self.INPUT_EMAIL).clear()
        self.driver.find_element(*self.INPUT_EMAIL).send_keys(email)

    def click_submit_your_information(self):
        self.driver.find_element(*self.BTN_SUBMIT_INFO).click()
