from seleniumpagefactory import PageFactory
from config.base import Config


class ThankYouPage(PageFactory):
    """Described 'ThankYouPage' page."""

    locators = {
        "heading": ("tag", 'h2'),
    }

    def __init__(self, driver):
        super().__init__()
        self.url = Config.URL + '?action=thankYou'
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)

    def grab_thank_you_message(self):
        return self.heading.text
