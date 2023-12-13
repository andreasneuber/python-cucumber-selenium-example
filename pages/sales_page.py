from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from config.base import Config


class SalesPage:
    """Described 'LoginPage' page."""

    HEADING_SALES = (By.XPATH, "//h2[contains(text(),'Sales - Statistics')]")
    HEADING_YEAR_MONTH = (By.CSS_SELECTOR, ".sales.header-year-month")
    CELL_MONTH = "//td[contains(text(), '%s')]"
    CELL_SALES_AMOUNT = "//td[contains(text(), '%s')]/following-sibling::td"

    def __init__(self, driver: Chrome):
        self.url = Config.URL + '?action=sales'
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)

    def sales_stats_page_is_displayed(self):
        element = self.driver.find_element(*self.HEADING_SALES)
        result = False

        if element.is_displayed():
            result = True

        return result

    def grab_year_month_header(self):
        return self.driver.find_element(*self.HEADING_YEAR_MONTH).text

    def month_cell_is_displayed(self, month):
        complete_xpath = self.CELL_MONTH % month
        element = self.driver.find_element(By.XPATH, complete_xpath)
        result = False

        if element.is_displayed():
            result = True

        return result

    def grab_sales_amount_from_month(self, month):
        complete_xpath = self.CELL_SALES_AMOUNT % month
        return self.driver.find_element(By.XPATH, complete_xpath).text
