Feature: Convert Celsius Feature
  Description: The purpose of this feature is to illustrate the usage of inline variables

  @inlineVars
  Scenario: Convert Celsius to correct Fahrenheit equivalent
    Given I provide "30" degree Celsius
    When I click the convert button
    Then I should see as result "86" Fahrenheit