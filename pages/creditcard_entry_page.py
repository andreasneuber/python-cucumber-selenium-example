from seleniumpagefactory.Pagefactory import PageFactory
from config.base import Config


class CreditCardEntryPage(PageFactory):
    """Described 'CreditCardEntryPage' page."""

    locators = {
        "input_cname": ('ID', 'cname'),
        "input_ccnum": ('ID', 'ccnum'),
        "input_expdate": ('ID', 'expdate'),
        "input_cvv": ('ID', 'cvv'),
        "btn_paynow": ('NAME', 'paynow'),
    }

    def __init__(self, driver):
        super().__init__()
        self.url = Config.URL + '?action=form3'
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)

    def enter_card_information(self, card_name, cc_number, expiry_date, cvv):
        self.input_cname.clear()
        self.input_cname.send_keys(card_name)

        self.input_ccnum.clear()
        self.input_ccnum.send_keys(cc_number)

        self.input_expdate.clear()
        self.input_expdate.send_keys(expiry_date)

        self.input_cvv.clear()
        self.input_cvv.send_keys(cvv)

    def submit_payment(self):
        self.btn_paynow.click()
