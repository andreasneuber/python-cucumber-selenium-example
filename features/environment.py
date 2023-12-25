from features.driverfactory import SeleniumDriverFactory
from config.base import Config
from pages.celsius_to_fahrenheit_page import CelsiusToFahrenheitPage
from pages.creditcard_entry_page import CreditCardEntryPage
from pages.creditcard_response_page import CreditCardResponsePage
from pages.employee_page import EmployeePage
from pages.login_page import LoginPage
from pages.provide_your_details_page import ProvideYourDetailsPage
from pages.sales_page import SalesPage
from pages.thank_you_page import ThankYouPage
from pages.user_account_page import UserAccountPage


def before_all(context):
    driver_factory = SeleniumDriverFactory(Config.BROWSER)
    context.browser = driver_factory.get_driver()

    # Pages
    context.celsius_to_fahrenheit_page = CelsiusToFahrenheitPage(context.browser)
    context.credit_card_entry_page = CreditCardEntryPage(context.browser)
    context.credit_card_response_page = CreditCardResponsePage(context.browser)
    context.employee_page = EmployeePage(context.browser)
    context.login_page = LoginPage(context.browser)
    context.provide_your_details_page = ProvideYourDetailsPage(context.browser)
    context.sales_page = SalesPage(context.browser)
    context.thank_you_page = ThankYouPage(context.browser)
    context.user_account_page = UserAccountPage(context.browser)


def after_all(context):
    context.browser.quit()
    del context


def before_feature(context, feature):
    if 'concurrentWindows' in feature.tags:
        print(feature.tags)
        print(feature.name)
        print(context)
