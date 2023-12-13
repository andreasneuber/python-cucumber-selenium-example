from behave import *
from pages.celsius_to_fahrenheit_page import CelsiusToFahrenheitPage
from assertpy import assert_that


@given(u'I provide "{celsius_degrees}" degree Celsius')
def step_impl(context, celsius_degrees):
    context.celsius_to_fahrenheit = CelsiusToFahrenheitPage(context.browser)
    context.celsius_to_fahrenheit.visit()
    context.celsius_to_fahrenheit.provide_celsius(celsius_degrees)


@when("I click the convert button")
def step_impl(context):
    context.celsius_to_fahrenheit = CelsiusToFahrenheitPage(context.browser)
    context.celsius_to_fahrenheit.click_convert()


@then('I should see as result "{expected_fahrenheit}" Fahrenheit')
def step_impl(context, expected_fahrenheit):
    context.celsius_to_fahrenheit = CelsiusToFahrenheitPage(context.browser)
    actual_fahrenheit = context.celsius_to_fahrenheit.read_fahrenheit_field()
    assert_that(actual_fahrenheit).is_equal_to(expected_fahrenheit)
