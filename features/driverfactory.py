from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService


class SeleniumDriverFactory:
    """Driver factory to provide a Selenium WebDriver for supported browsers."""

    def __init__(self, browser='firefox', headless=False):
        self.browser = browser.lower()
        self.headless = headless

    def get_driver(self):
        driver_method = getattr(self, f"_get_{self.browser}_driver", None)
        if callable(driver_method):
            return driver_method()
        raise ValueError(f"Unsupported browser: {self.browser}")

    def _get_firefox_driver(self):
        options = FirefoxOptions()
        if self.headless:
            options.add_argument("--headless")

        profile = webdriver.FirefoxProfile()
        profile.set_preference('app.update.auto', False)
        profile.set_preference('app.update.enabled', False)
        profile.set_preference('app.update.silent', False)
        options.profile = profile

        service = FirefoxService()
        return webdriver.Firefox(service=service, options=options)

    def _get_chrome_driver(self):
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--no-sandbox")
        if self.headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1420,1080")

        service = ChromeService()
        return webdriver.Chrome(service=service, options=options)

    def _get_edge_driver(self):
        options = EdgeOptions()
        options.add_argument("--start-maximized")
        if self.headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1420,1080")

        service = EdgeService()
        return webdriver.Edge(service=service, options=options)
