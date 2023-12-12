from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class UserAccountPage:
    """Described 'UserAccountPage' page."""

    HEADING_ADMIN_DASHBOARD = (By.XPATH, "//h2[contains(text(),'Admin Dashboard')]")
    LINK_HR_SECTION = (By.ID, "hr-resources-link")
    LINK_SALES_SECTION = (By.ID, "sales-statistics-link")

    def __init__(self, driver: Chrome, config):
        self.url = config['env']['base_url'] + '?action=useraccount'
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)

    def admin_dashboard_is_displayed(self):
        element = self.driver.find_element(*self.HEADING_ADMIN_DASHBOARD)
        result = False

        if element.is_displayed():
            result = True

        return result

    def navigate_to_hr_section(self):
        self.driver.find_element(*self.LINK_HR_SECTION).click()

    def navigate_to_sales_section(self):
        self.driver.find_element(*self.LINK_SALES_SECTION).click()
