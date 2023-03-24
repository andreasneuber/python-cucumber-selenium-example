from selenium.webdriver import Chrome


class ThankYouPage:
    """Described 'ThankYouPage' page."""

    def __init__(self, driver: Chrome, config):
        self.url = config['env']['base_url'] + '?action=thankYou'
        self._driver = driver

    def visit(self):
        self._driver.get(self.url)

    def grab_thank_you_message(self):
        return self._driver.find_element_by_tag_name("h2").text
