from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from config.base import Config


class ThankYouPage:
    """Described 'ThankYouPage' page."""

    HEADING = (By.TAG_NAME, "h2")

    def __init__(self, driver: Chrome):
        self.url = Config.URL + '?action=thankYou'
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)

    def grab_thank_you_message(self):
        return self.driver.find_element(*self.HEADING).text
