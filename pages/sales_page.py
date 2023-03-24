from selenium.webdriver import Chrome


class SalesPage:
    """Described 'LoginPage' page."""

    def __init__(self, driver: Chrome, config):
        self.url = config['env']['base_url'] + '?action=sales'
        self._driver = driver

    def visit(self):
        self._driver.get(self.url)

    def sales_stats_page_is_displayed(self):
        element = self._driver.find_element_by_xpath("//h2[contains(text(),'Sales - Statistics')]")
        result = False

        if element.is_displayed():
            result = True

        return result

    def grab_year_month_header(self):
        return self._driver.find_element_by_css_selector(".sales.header-year-month").text

    def month_cell_is_displayed(self, month):
        complete_xpath = "//td[contains(text(), '%s')]" % month
        element = self._driver.find_element_by_xpath(complete_xpath)
        result = False

        if element.is_displayed():
            result = True

        return result

    def grab_sales_amount_from_month(self, month):
        complete_xpath = "//td[contains(text(), '%s')]/following-sibling::td" % month
        return self._driver.find_element_by_xpath(complete_xpath).text
