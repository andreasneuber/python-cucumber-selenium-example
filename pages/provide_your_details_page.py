from selenium.webdriver import Chrome


class ProvideYourDetailsPage:
    """Described 'ProvideYourDetailsPage' page."""

    def __init__(self, driver: Chrome, config):
        self.url = config['env']['base_url'] + '?action=form1'
        self._driver = driver

    def visit(self):
        self._driver.get(self.url)

    def provide_first_name(self, first_name):
        element = self._driver.find_element_by_id("fname")
        element.clear()
        element.send_keys(first_name)

    def provide_last_name(self, last_name):
        element = self._driver.find_element_by_id("lname")
        element.clear()
        element.send_keys(last_name)

    def provide_street(self, street):
        element = self._driver.find_element_by_id("street")
        element.clear()
        element.send_keys(street)

    def provide_city(self, city):
        element = self._driver.find_element_by_id("city")
        element.clear()
        element.send_keys(city)

    def provide_zip(self, zip_code):
        element = self._driver.find_element_by_id("zip")
        element.clear()
        element.send_keys(zip_code)

    def provide_state(self, state):
        element = self._driver.find_element_by_id("state")
        element.clear()
        element.send_keys(state)

    def provide_country(self, country):
        element = self._driver.find_element_by_id("country")
        element.clear()
        element.send_keys(country)

    def provide_mobile_phone_number(self, number):
        element = self._driver.find_element_by_id("mobile")
        element.clear()
        element.send_keys(number)

    def provide_home_phone_number(self, number):
        element = self._driver.find_element_by_id("home")
        element.clear()
        element.send_keys(number)

    def provide_email(self, email):
        element = self._driver.find_element_by_id("email")
        element.clear()
        element.send_keys(email)

    def click_submit_your_information(self):
        self._driver.find_element_by_id("submit-info").click()
