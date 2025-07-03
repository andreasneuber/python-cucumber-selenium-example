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
    try:
        driver_factory = SeleniumDriverFactory(Config.BROWSER)
        context.browser = driver_factory.get_driver()
        init_pages(context, context.browser)

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

    except Exception as e:
        print(f"[ERROR] Failed to initialize browser: {e}")
        context.browser = None
        raise


def init_pages(context, browser):
    page_classes = {
        'celsius_to_fahrenheit_page': CelsiusToFahrenheitPage,
        'credit_card_entry_page': CreditCardEntryPage,
        'credit_card_response_page': CreditCardResponsePage,
        'employee_page': EmployeePage,
        'login_page': LoginPage,
        'provide_your_details_page': ProvideYourDetailsPage,
        'sales_page': SalesPage,
        'thank_you_page': ThankYouPage,
        'user_account_page': UserAccountPage,
    }

    for name, cls in page_classes.items():
        setattr(context, name, cls(browser))


def after_all(context):
    if hasattr(context, "browser") and context.browser:
        context.browser.quit()
    del context


def before_feature(context, feature):
    if 'concurrentWindows' in feature.tags:
        print(feature.tags)
        print(feature.name)
        print(context)
