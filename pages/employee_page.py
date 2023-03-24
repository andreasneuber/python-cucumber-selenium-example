from selenium.webdriver import Chrome


class EmployeePage:
    """Described 'EmployeePage' page."""

    def __init__(self, driver: Chrome, config):
        self.url = config['env']['base_url'] + '?action=employee'
        self._driver = driver

    def visit(self):
        self._driver.get(self.url)

    def employee_page_is_displayed(self):
        element = self._driver.find_element_by_xpath("//h2[contains(text(),'Human Resources - Find employee')]")
        result = False

        if element.is_displayed():
            result = True

        return result

    def fill_employee_name_input(self, employee_name):
        element = self._driver.find_element_by_id("employee-name")
        element.clear()
        element.send_keys(employee_name)

    def click_search_btn(self):
        self._driver.find_element_by_id("btnSearch").click()

    def employee_record_is_displayed(self):
        element = self._driver.find_element_by_id("employee-details")
        result = False

        if element.is_displayed():
            result = True

        return result

    def grab_employee_name(self):
        return self._driver.find_element_by_css_selector(".employee.name").text

    def grab_department_name(self):
        return self._driver.find_element_by_css_selector(".employee.department").text
