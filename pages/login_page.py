from selenium.webdriver import Chrome


class LoginPage:
    """Described 'LoginPage' page."""

    def __init__(self, driver: Chrome, config):
        self.url = config['env']['base_url'] + '?action=form4'
        self._driver = driver

    def visit(self):
        self._driver.get(self.url)

    def provide_username(self, user_name):
        element = self._driver.find_element_by_name("user")
        element.clear()
        element.send_keys(user_name)

    def provide_password(self, password):
        element = self._driver.find_element_by_name("pw")
        element.clear()
        element.send_keys(password)

    def login(self, user_name, password):
        self.provide_username(user_name)
        self.provide_password(password)
        self.click_login()

    def click_login(self):
        self._driver.find_element_by_name("Login").click()
