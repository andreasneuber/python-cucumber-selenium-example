from selenium.webdriver import Chrome


class CreditCardEntryPage:
    """Described 'CreditCardEntryPage' page."""

    def __init__(self, driver: Chrome, config):
        self.url = config['env']['base_url'] + '?action=form3'
        self._driver = driver

    def visit(self):
        self._driver.get(self.url)

    def enter_card_information(self, card_name, cc_number, expiry_date, cvv):
        element = self._driver.find_element_by_id("cname")
        element.clear()
        element.send_keys(card_name)

        element = self._driver.find_element_by_id("ccnum")
        element.clear()
        element.send_keys(cc_number)

        element = self._driver.find_element_by_id("expdate")
        element.clear()
        element.send_keys(expiry_date)

        element = self._driver.find_element_by_id("cvv")
        element.clear()
        element.send_keys(cvv)

    def submit_payment(self):
        self._driver.find_element_by_name("paynow").click()
