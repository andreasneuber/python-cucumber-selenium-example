from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class CelsiusToFahrenheitPage:
    """Described 'CelsiusToFahrenheit' page."""

    INPUT_CELSIUS = (By.NAME, "celsius")
    BTN_CELSIUS = (By.ID, "btnCelsius")
    INPUT_FAHRENHEIT = (By.NAME, "fahrenheit")

    def __init__(self, driver: Chrome, config):
        self.url = config['env']['base_url'] + '?action=form6'
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)

    def provide_celsius(self, celsius_degrees):
        self.driver.find_element(*self.INPUT_CELSIUS).clear()
        self.driver.find_element(*self.INPUT_CELSIUS).send_keys(celsius_degrees)

    def click_convert(self):
        self.driver.find_element(*self.BTN_CELSIUS).click()

    def read_fahrenheit_field(self):
        return self.driver.find_element(*self.INPUT_FAHRENHEIT).get_attribute("value")
