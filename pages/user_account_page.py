from selenium.webdriver import Chrome


class UserAccountPage:
    """Described 'UserAccountPage' page."""

    def __init__(self, driver: Chrome, config):
        self.url = config['env']['base_url'] + '?action=useraccount'
        self._driver = driver

    def visit(self):
        self._driver.get(self.url)

    def admin_dashboard_is_displayed(self):
        element = self._driver.find_element_by_xpath("//h2[contains(text(),'Admin Dashboard')]")
        result = False

        if element.is_displayed():
            result = True

        return result

    def navigate_to_hr_section(self):
        self._driver.find_element_by_id("hr-resources-link").click()

    def navigate_to_sales_section(self):
        self._driver.find_element_by_id("sales-statistics-link").click()
