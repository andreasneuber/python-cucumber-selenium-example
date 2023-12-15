Feature: Login Feature
  Description: The purpose of this feature is to illustrate the usage of horizontal and vertical data tables

  @horizontalTable
  Scenario: Login with correct credential
    Given I navigate to login page
    And I enter following for login
      | username | password |
      | admin    | pw1234   |
    When I click login button
    Then I should be able to access the protected area

  @verticalTable
  Scenario: Login with correct credentials
    Given I navigate to login page
    And I enter following values to login
      | field    | value  |
      | username | admin  |
      | password | pw1234 |
    When I click login button
    Then I should be able to access the protected area