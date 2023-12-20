from seleniumpagefactory.Pagefactory import PageFactory
from config.base import Config


class CreditCardResponsePage(PageFactory):
    """Described 'CreditCardResponsePage' page."""

    locators = {
        "alert_box": ('XPATH', "//div[contains(@class, 'alert')]"),
        "response_txt": ('XPATH', "//strong[@class='response']"),
        "more_info_txt": ('CLASS_NAME', 'more-info'),
    }

    def __init__(self, driver):
        super().__init__()
        self.url = Config.URL + '?action=responsecc'
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)

    def alert_message_box_is_displayed(self):
        return True if self.alert_box.is_displayed() else False

    def grab_response_from_alert_box(self):
        return self.response_txt.text

    def grab_more_info_from_alert_box(self):
        return self.more_info_txt.text
