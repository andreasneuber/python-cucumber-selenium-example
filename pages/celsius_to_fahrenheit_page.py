from seleniumpagefactory.Pagefactory import PageFactory
from config.base import Config


class CelsiusToFahrenheitPage(PageFactory):
    """Described 'CelsiusToFahrenheit' page."""

    locators = {
        "input_celsius": ('NAME', 'celsius'),
        "btn_celsius": ('ID', 'btnCelsius'),
        "input_fahrenheit": ('NAME', 'fahrenheit'),
    }

    def __init__(self, driver):
        super().__init__()
        self.url = Config.URL + '?action=form6'
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)

    def provide_celsius(self, celsius_degrees):
        self.input_celsius.clear()
        self.input_celsius.send_keys(celsius_degrees)

    def click_convert(self):
        self.btn_celsius.click()

    def read_fahrenheit_field(self):
        return self.input_fahrenheit.get_attribute("value")
