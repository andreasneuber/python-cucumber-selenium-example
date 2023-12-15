Feature: Admin Privileges
  Description: The purpose of this feature is to illustrate the usage of the Background keyword


  Background: Admin User is Logged In
    Given I navigate to login page
    When I submit username "admin" and password "pw1234"
    Then I will be logged into the Admin Dashboard

  @background
  Scenario: Admin can access Human Resources records
    When Admin searches for employee "Joe Doe"
    Then information appears that employee "Joe Doe" belongs to department "Marketing"

  @background
  Scenario: Admin can access Sales statistics
    When Admin looks up total sales amount for month "June" in year "2022"
    Then the total "June" sales amount is "32164"