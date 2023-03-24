from behave import *
from pages.login_page import LoginPage
from pages.user_account_page import UserAccountPage
from assertpy import assert_that


@step("I enter following for login")
def step_impl(context):
    context.login_page = LoginPage(context.browser, context.config)
    context.login_page.provide_username(context.table[0]["username"])
    context.login_page.provide_password(context.table[0]["password"])


@when("I click login button")
def step_impl(context):
    context.login_page = LoginPage(context.browser, context.config)
    context.login_page.click_login()


@step("I enter following values to login")
def step_impl(context):
    context.login_page = LoginPage(context.browser, context.config)
    context.login_page.provide_username(context.table[0]["value"])
    context.login_page.provide_password(context.table[1]["value"])


@then("I should be able to access the protected area")
def step_impl(context):
    context.user_account_page = UserAccountPage(context.browser, context.config)
    visible = context.user_account_page.admin_dashboard_is_displayed()
    assert_that(visible).is_true()
