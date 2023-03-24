import os
import yaml

from selenium import webdriver


def before_all(context):
    options = webdriver.ChromeOptions()

    # Optimized for local development
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")

    # Optimized for running tests in CI pipelines
    # options.add_argument("--start-maximized")
    # options.add_argument("--no-sandbox")
    # options.add_argument('--window-size=1420,1080')
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')

    context.browser = webdriver.Chrome(chrome_options=options)

    context.error_message = "Element not found"

    context.config = None
    with open(os.getcwd() + os.path.sep + "config.yml", 'r') as ymlfile:
        context.config = yaml.load(ymlfile, Loader=yaml.Loader)


def after_all(context):
    context.browser.quit()


def before_feature(context, feature):
    if 'concurrentWindows' in feature.tags:
        print(feature.tags)
        print(feature.name)
        print(context)
