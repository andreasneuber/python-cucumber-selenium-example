from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class CreditCardResponsePage:
    """Described 'CreditCardResponsePage' page."""

    ALERT_BOX = (By.XPATH, "//div[contains(@class, 'alert')]")
    RESPONSE_TXT = (By.XPATH, "//strong[@class='response']")
    MORE_INFO_TXT = (By.CLASS_NAME, 'more-info')

    def __init__(self, driver: Chrome, config):
        self.url = config['env']['base_url'] + '?action=responsecc'
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)

    def alert_message_box_is_displayed(self):
        element = self.driver.find_element(*self.ALERT_BOX)
        result = False

        if element.is_displayed():
            result = True

        return result

    def grab_response_from_alert_box(self):
        return self.driver.find_element(*self.RESPONSE_TXT).text

    def grab_more_info_from_alert_box(self):
        return self.driver.find_element(*self.MORE_INFO_TXT).text
