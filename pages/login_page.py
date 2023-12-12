from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class LoginPage:
    """Described 'LoginPage' page."""

    INPUT_USERNAME = (By.NAME, "user")
    INPUT_PASSWORD = (By.NAME, "pw")
    BTN_LOGIN = (By.NAME, "Login")

    def __init__(self, driver: Chrome, config):
        self.url = config['env']['base_url'] + '?action=form4'
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)

    def provide_username(self, user_name):
        self.driver.find_element(*self.INPUT_USERNAME).clear()
        self.driver.find_element(*self.INPUT_USERNAME).send_keys(user_name)

    def provide_password(self, password):
        self.driver.find_element(*self.INPUT_PASSWORD).clear()
        self.driver.find_element(*self.INPUT_PASSWORD).send_keys(password)

    def login(self, user_name, password):
        self.provide_username(user_name)
        self.provide_password(password)
        self.click_login()

    def click_login(self):
        self.driver.find_element(*self.BTN_LOGIN).click()
