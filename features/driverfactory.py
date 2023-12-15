from selenium import webdriver


class SeleniumDriverFactory(object):
    """Driver factory to provide driver for running tests on web browsers.
    """

    def __init__(self, browser='firefox'):
        self.browser = browser

    def get_driver(self):
        # Call the method as we return it
        web_driver = getattr(self, self.browser)
        return web_driver()

    @staticmethod
    def firefox():
        profile = webdriver.FirefoxProfile()
        profile.set_preference('app.update.auto', False)
        profile.set_preference('app.update.enabled', False)
        profile.set_preference('app.update.silent', False)

        return webdriver.Firefox(profile)

    @staticmethod
    def chrome():
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--no-sandbox")

        # Optimized for running tests in CI pipelines
        # options.add_argument("--start-maximized")
        # options.add_argument("--no-sandbox")
        # options.add_argument('--window-size=1420,1080')
        # options.add_argument('--headless')
        # options.add_argument('--disable-gpu')

        return webdriver.Chrome(chrome_options=options)
