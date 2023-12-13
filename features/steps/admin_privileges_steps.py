from behave import *
from pages.login_page import LoginPage
from pages.user_account_page import UserAccountPage
from pages.employee_page import EmployeePage
from pages.sales_page import SalesPage
from assertpy import assert_that


@given("I navigate to login page")
def step_impl(context):
    context.login_page = LoginPage(context.browser)
    context.login_page.visit()


@when('I submit username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page = LoginPage(context.browser)
    context.login_page.login(username, password)


@then("I will be logged into the Admin Dashboard")
def step_impl(context):
    context.user_account_page = UserAccountPage(context.browser)
    visible = context.user_account_page.admin_dashboard_is_displayed()
    assert_that(visible).is_true()


@when('Admin searches for employee "{employee_name}"')
def step_impl(context, employee_name):
    context.user_account_page = UserAccountPage(context.browser)
    context.user_account_page.navigate_to_hr_section()

    context.employee_page = EmployeePage(context.browser)
    visible = context.employee_page.employee_page_is_displayed()
    assert_that(visible).is_true()

    context.employee_page.fill_employee_name_input(employee_name)
    context.employee_page.click_search_btn()


@then('information appears that employee "{expected_employee_name}" belongs to department "{expected_department_name}"')
def step_impl(context, expected_employee_name, expected_department_name):
    context.employee_page = EmployeePage(context.browser)

    visible = context.employee_page.employee_record_is_displayed
    assert_that(visible).is_true()

    actual_employee_name = context.employee_page.grab_employee_name()
    assert_that(actual_employee_name).is_equal_to(expected_employee_name)

    actual_department_name = context.employee_page.grab_department_name()
    assert_that(actual_department_name).is_equal_to(expected_department_name)


@when('Admin looks up total sales amount for month "{month}" in year "{year}"')
def step_impl(context, month, year):
    context.user_account_page = UserAccountPage(context.browser)
    context.user_account_page.navigate_to_sales_section()

    context.sales_page = SalesPage(context.browser)
    visible = context.sales_page.sales_stats_page_is_displayed()
    assert_that(visible).is_true()

    year_month_header = context.sales_page.grab_year_month_header()
    assert_that(year_month_header).starts_with(year)

    visible = context.sales_page.month_cell_is_displayed(month)
    assert_that(visible).is_true()


@then('the total "{month}" sales amount is "{expected_sales_amount}"')
def step_impl(context, month, expected_sales_amount):
    context.sales_page = SalesPage(context.browser)

    actual_sales_amount = context.sales_page.grab_sales_amount_from_month(month)
    assert_that(actual_sales_amount).is_equal_to(expected_sales_amount)
