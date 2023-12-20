from seleniumpagefactory.Pagefactory import PageFactory
from config.base import Config


class LoginPage(PageFactory):
    """Described 'LoginPage' page."""

    locators = {
        "input_username": ('NAME', 'user'),
        "input_password": ('NAME', 'pw'),
        "btn_login": ('NAME', 'Login')
    }

    def __init__(self, driver):
        super().__init__()
        self.url = Config.URL + '?action=form4'
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)

    def provide_username(self, user_name):
        self.input_username.clear()
        self.input_username.send_keys(user_name)

    def provide_password(self, password):
        self.input_password.clear()
        self.input_password.send_keys(password)

    def login(self, user_name, password):
        self.provide_username(user_name)
        self.provide_password(password)
        self.click_login()

    def click_login(self):
        self.btn_login.click()
