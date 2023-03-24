# python-cucumber-selenium-framework
Sample implementation for Python Behave

## Setup
`pip install -r requirements.txt`

## Run specific tests locally
`behave --tags=data_table`

- or -

`behave --tags=inlineVars`

- or -

`behave --tags=background`

- or -

`behave --tags=scenarioOutline`

- or -

`behave --tags=horizontalTable`

- or -

`behave --tags=verticalTable`

- or -

`behave --tags=verticalTableLong`

## Run locally with Allure reports
On Windows install Allure: `scoop install allure`

`behave -f allure_behave.formatter:AllureFormatter -o ./reports/allure  ./features`

`allure serve reports/allure`

## Updating
`pip install -U behave`

