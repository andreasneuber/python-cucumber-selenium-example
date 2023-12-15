Feature: Provide Your Details Feature
  Description: The purpose of this feature is to illustrate the usage of a long vertical table

  @verticalTableLong
  Scenario: Submit address and communication details
    Given I navigate to Information about yourself page
    When I provide the following details
      | field        | value             |
      | firstname    | Joe               |
      | lastname     | Doe               |
      | street       | 10 Example Street |
      | city         | Sample Town       |
      | zip          | 99999             |
      | state        | Great State       |
      | country      | USA               |
      | mobile phone | 123-456-789       |
      | home phone   | 987-654-321       |
      | email        | joe@example.com   |
    Then I will see message "Thank you!"