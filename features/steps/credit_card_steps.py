from behave import *
from assertpy import assert_that


@given("User is on credit card entry page")
def step_impl(context):
    context.credit_card_entry_page.visit()


@when('User "{name}" enters card number "{cc_number}" together with expiry date "{exp_date}" and cvv "{cvv}"')
def step_impl(context, name, cc_number, exp_date, cvv):
    context.credit_card_entry_page.enter_card_information(name, cc_number, exp_date, cvv)
    context.credit_card_entry_page.submit_payment()


@then('the page will respond with "{expected_response}" and provide as reason "{expected_reason}"')
def step_impl(context, expected_response, expected_reason):
    visible = context.credit_card_response_page.alert_message_box_is_displayed()
    assert_that(visible).is_true()

    actual_response = context.credit_card_response_page.grab_response_from_alert_box()
    assert_that(actual_response).starts_with(expected_response)

    actual_reason = context.credit_card_response_page.grab_more_info_from_alert_box()
    assert_that(actual_reason).contains(expected_reason)
