from behave import *
from assertpy import assert_that


@given(u'I provide "{celsius_degrees}" degree Celsius')
def step_impl(context, celsius_degrees):
    context.celsius_to_fahrenheit_page.visit()
    context.celsius_to_fahrenheit_page.provide_celsius(celsius_degrees)


@when("I click the convert button")
def step_impl(context):
    context.celsius_to_fahrenheit_page.click_convert()


@then('I should see as result "{expected_fahrenheit}" Fahrenheit')
def step_impl(context, expected_fahrenheit):
    actual_fahrenheit = context.celsius_to_fahrenheit_page.read_fahrenheit_field()
    assert_that(actual_fahrenheit).is_equal_to(expected_fahrenheit)
