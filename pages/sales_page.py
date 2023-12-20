from selenium.webdriver.common.by import By
from seleniumpagefactory import PageFactory

from config.base import Config


class SalesPage(PageFactory):
    """Described 'LoginPage' page."""

    locators = {
        "heading_sales": ('XPATH', "//h2[contains(text(),'Sales - Statistics')]"),
        "heading_year_month": ('CSS', ".sales.header-year-month"),
    }

    raw_locators = {
        "cell_month": "//td[contains(text(), '%s')]",
        "cell_sales_amount": "//td[contains(text(), '%s')]/following-sibling::td",
    }

    def __init__(self, driver):
        super().__init__()
        self.url = Config.URL + '?action=sales'
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)

    def sales_stats_page_is_displayed(self):
        return True if self.heading_sales.is_displayed() else False

    def grab_year_month_header(self):
        return self.heading_year_month.text

    def month_cell_is_displayed(self, month):
        complete_xpath = self.raw_locators['cell_month'] % month
        element = self.driver.find_element(By.XPATH, complete_xpath)
        return True if element.is_displayed() else False

    def grab_sales_amount_from_month(self, month):
        complete_xpath = self.raw_locators['cell_sales_amount'] % month
        return self.driver.find_element(By.XPATH, complete_xpath).text
