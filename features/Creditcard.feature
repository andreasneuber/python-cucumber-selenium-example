Feature: Creditcard Feature
  Description: The purpose of this feature is to illustrate the usage of a scenario outline

  @scenarioOutline
  Scenario Outline: Different responses to credit card data input
    Given User is on credit card entry page
    When User "<name>" enters card number "<cc-number>" together with expiry date "<expiry-date>" and cvv "<cvv>"
    Then the page will respond with "<response>" and provide as reason "<reason>"

    Examples:
      | name         | cc-number        | expiry-date | cvv | response | reason                      |
      | Joe Doe      | 4242424242424242 | 10/27       | 753 | Success  | You are using VISA          |
      | Hans Hansen  | 5555555555554444 | 02/28       | 159 | Success  | You are using MASTERCARD    |
      | Eugene Tonya | 4000000000009995 | 07/26       | 741 | Declined | You have insufficient funds |