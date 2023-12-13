from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from config.base import Config


class EmployeePage:
    """Described 'EmployeePage' page."""

    HEADING_HR = (By.XPATH, "//h2[contains(text(),'Human Resources - Find employee')]")
    INPUT_EMPLOYEE_NAME = (By.ID, 'employee-name')
    BTN_SEARCH = (By.ID, 'btnSearch')
    EMPLOYEE_RECORD = (By.ID, 'employee-details')
    EMPLOYEE_NAME = (By.CSS_SELECTOR, '.employee.name')
    EMPLOYEE_DEPARTMENT = (By.CSS_SELECTOR, '.employee.department')

    def __init__(self, driver: Chrome):
        self.url = Config.URL + '?action=employee'
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)

    def employee_page_is_displayed(self):
        element = self.driver.find_element(*self.HEADING_HR)
        result = False

        if element.is_displayed():
            result = True

        return result

    def fill_employee_name_input(self, employee_name):
        self.driver.find_element(*self.INPUT_EMPLOYEE_NAME).clear()
        self.driver.find_element(*self.INPUT_EMPLOYEE_NAME).send_keys(employee_name)

    def click_search_btn(self):
        self.driver.find_element(*self.BTN_SEARCH).click()

    def employee_record_is_displayed(self):
        element = self.driver.find_element(*self.EMPLOYEE_RECORD)
        result = False

        if element.is_displayed():
            result = True

        return result

    def grab_employee_name(self):
        return self.driver.find_element(*self.EMPLOYEE_NAME).text

    def grab_department_name(self):
        return self.driver.find_element(*self.EMPLOYEE_DEPARTMENT).text
