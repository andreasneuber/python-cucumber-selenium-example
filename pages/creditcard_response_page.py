from selenium.webdriver import Chrome


class CreditCardResponsePage:
    """Described 'CreditCardResponsePage' page."""

    def __init__(self, driver: Chrome, config):
        self.url = config['env']['base_url'] + '?action=responsecc'
        self._driver = driver

    def visit(self):
        self._driver.get(self.url)

    def alert_message_box_is_displayed(self):
        element = self._driver.find_element_by_xpath("//div[contains(@class, 'alert')]")
        result = False

        if element.is_displayed():
            result = True

        return result

    def grab_response_from_alert_box(self):
        return self._driver.find_element_by_xpath("//strong[@class='response']").text

    def grab_more_info_from_alert_box(self):
        return self._driver.find_element_by_css_selector(".more-info").text
