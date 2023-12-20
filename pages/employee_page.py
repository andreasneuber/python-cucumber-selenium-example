from seleniumpagefactory.Pagefactory import PageFactory
from config.base import Config


class EmployeePage(PageFactory):
    """Described 'EmployeePage' page."""

    locators = {
        "heading_hr": ('XPATH', "//h2[contains(text(),'Human Resources - Find employee')]"),
        "input_employee_name": ('ID', "employee-name"),
        "btn_search": ('ID', "btnSearch"),
        "employee_record": ('ID', "employee-details"),
        "employee_name": ('CSS', ".employee.name"),
        "employee_department": ('CSS', ".employee.department"),
    }

    def __init__(self, driver):
        super().__init__()
        self.url = Config.URL + '?action=employee'
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)

    def employee_page_is_displayed(self):
        return True if self.heading_hr.is_displayed() else False

    def fill_employee_name_input(self, employee_name):
        self.input_employee_name.clear()
        self.input_employee_name.send_keys(employee_name)

    def click_search_btn(self):
        self.btn_search.click()

    def employee_record_is_displayed(self):
        return True if self.employee_record.is_displayed() else False

    def grab_employee_name(self):
        return self.employee_name.text

    def grab_department_name(self):
        return self.employee_department.text
