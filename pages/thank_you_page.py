from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class ThankYouPage:
    """Described 'ThankYouPage' page."""

    HEADING = (By.TAG_NAME, "h2")

    def __init__(self, driver: Chrome, config):
        self.url = config['env']['base_url'] + '?action=thankYou'
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)

    def grab_thank_you_message(self):
        return self.driver.find_element(*self.HEADING).text
