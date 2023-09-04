# python-cucumber-selenium-example
Sample implementation of Python Behave

## Application under test
The feature files, step definitions and page objects were written for https://github.com/andreasneuber/automatic-test-sample-site.
Readme in that repo has further details how to set it up.

## Setup
`pip install -r requirements.txt`

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

## Updating
`pip install -U behave`
