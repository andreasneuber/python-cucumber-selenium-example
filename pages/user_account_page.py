from seleniumpagefactory import PageFactory
from config.base import Config


class UserAccountPage(PageFactory):
    """Described 'UserAccountPage' page."""

    locators = {
        "heading_admin_dashboard": ('XPATH', "//h2[contains(text(),'Admin Dashboard')]"),
        "link_hr_section": ('ID', "hr-resources-link"),
        "link_sales_section": ('ID', "sales-statistics-link"),
    }

    def __init__(self, driver):
        super().__init__()
        self.url = Config.URL + '?action=useraccount'
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)

    def admin_dashboard_is_displayed(self):
        return True if self.heading_admin_dashboard.is_displayed() else False

    def navigate_to_hr_section(self):
        self.link_hr_section.click()

    def navigate_to_sales_section(self):
        self.link_sales_section.click()
