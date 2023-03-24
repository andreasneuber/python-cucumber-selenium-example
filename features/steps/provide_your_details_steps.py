from behave import *
from pages.provide_your_details_page import ProvideYourDetailsPage
from pages.thank_you_page import ThankYouPage
from assertpy import assert_that


@given("I navigate to Information about yourself page")
def step_impl(context):
    context.provide_your_details_page = ProvideYourDetailsPage(context.browser, context.config)
    context.provide_your_details_page.visit()


@when("I provide the following details")
def step_impl(context):
    context.provide_your_details_page = ProvideYourDetailsPage(context.browser, context.config)

    for row in context.table:
        if row["field"] == "firstname":
            context.provide_your_details_page.provide_first_name(row["value"])
        elif row["field"] == "lastname":
            context.provide_your_details_page.provide_last_name(row["value"])
        elif row["field"] == "street":
            context.provide_your_details_page.provide_street(row["value"])
        elif row["field"] == "city":
            context.provide_your_details_page.provide_city(row["value"])
        elif row["field"] == "zip":
            context.provide_your_details_page.provide_zip(row["value"])
        elif row["field"] == "state":
            context.provide_your_details_page.provide_state(row["value"])
        elif row["field"] == "country":
            context.provide_your_details_page.provide_country(row["value"])
        elif row["field"] == "mobile phone":
            context.provide_your_details_page.provide_mobile_phone_number(row["value"])
        elif row["field"] == "home phone":
            context.provide_your_details_page.provide_home_phone_number(row["value"])
        elif row["field"] == "email":
            context.provide_your_details_page.provide_email(row["value"])
        else:
            "Do sth else"

    context.provide_your_details_page.click_submit_your_information()


@then('I will see message "{expected_message}"')
def step_impl(context, expected_message):
    context.thank_you_page = ThankYouPage(context.browser, context.config)
    actual_message = context.thank_you_page.grab_thank_you_message()
    assert_that(actual_message).is_equal_to(expected_message)
