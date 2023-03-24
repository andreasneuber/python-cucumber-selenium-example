from selenium.webdriver import Chrome


class CelsiusToFahrenheitPage:
    """Described 'CelsiusToFahrenheit' page."""

    def __init__(self, driver: Chrome, config):
        self.url = config['env']['base_url'] + '?action=form6'
        self._driver = driver

    def visit(self):
        self._driver.get(self.url)

    def provide_celsius(self, celsius_degrees):
        element = self._driver.find_element_by_name("celsius")
        element.clear()
        element.send_keys(celsius_degrees)

    def click_convert(self):
        self._driver.find_element_by_id("btnCelsius").click()

    def read_fahrenheit_field(self):
        return self._driver.find_element_by_name("fahrenheit").get_attribute("value")
