# python-cucumber-selenium-example
Sample implementation of Python Behave

## Application under test
The feature files, step definitions and page objects were written for https://github.com/andreasneuber/automatic-test-sample-site.
Readme in that repo has further details how to set it up.

## Setup - Windows 11 machine
- IDE used: PyCharm
- Install Python, with Windows installer - https://www.python.org/downloads/windows/
- In Pycharm set your new local Python executable as Interpreter
- Create a virtual environment: `py -m venv .venv`
- Activate virtual environment: `.venv\Scripts\activate`
- Double-check virtual environment: `pip --version`
- Install required Python packages: `pip install -r requirements.txt`

## Run all tests locally
`behave`

## Run specific tests locally
`behave --tags=data_table`

or

`behave --tags=inlineVars`

or

`behave --tags=background`

or

`behave --tags=scenarioOutline`

or

`behave --tags=horizontalTable`

or

`behave --tags=verticalTable`

or

`behave --tags=verticalTableLong`

## Run locally with Allure reports
Install Allure: https://docs.qameta.io/allure/#_get_started

`behave -f allure_behave.formatter:AllureFormatter -o ./reports/allure  ./features`

`allure serve reports/allure`

## More Configuration Possibilities
https://behave.readthedocs.io/en/stable/behave.html#configuration-files

## Updating Behave
`pip install -U behave`

## Wait Mechanism
Important subject - currently example uses functionality of the selenium-page-factory package.
Please see also "Note" box [here](https://selenium-page-factory.readthedocs.io/en/latest/#extended-webelements-methods).


### See also
https://github.com/the-creative-tester/python-behave-web-browser-automation-example

https://selenium-page-factory.readthedocs.io/en/latest/