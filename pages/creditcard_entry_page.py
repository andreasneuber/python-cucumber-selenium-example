from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from config.base import Config


class CreditCardEntryPage:
    """Described 'CreditCardEntryPage' page."""

    INPUT_CNAME = (By.ID, "cname")
    INPUT_CCNUM = (By.ID, "ccnum")
    INPUT_EXPDATE = (By.ID, "expdate")
    INPUT_CVV = (By.ID, "cvv")
    BTN_PAYNOW = (By.NAME, "paynow")

    def __init__(self, driver: Chrome):
        self.url = Config.URL + '?action=form3'
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)

    def enter_card_information(self, card_name, cc_number, expiry_date, cvv):
        self.driver.find_element(*self.INPUT_CNAME).clear()
        self.driver.find_element(*self.INPUT_CNAME).send_keys(card_name)

        self.driver.find_element(*self.INPUT_CCNUM).clear()
        self.driver.find_element(*self.INPUT_CCNUM).send_keys(cc_number)

        self.driver.find_element(*self.INPUT_EXPDATE).clear()
        self.driver.find_element(*self.INPUT_EXPDATE).send_keys(expiry_date)

        self.driver.find_element(*self.INPUT_CVV).clear()
        self.driver.find_element(*self.INPUT_CVV).send_keys(cvv)

    def submit_payment(self):
        self.driver.find_element(*self.BTN_PAYNOW).click()
