Feature: This test to cover Login feature example in Sauce Demo site

  Scenario: Run login test cases example
    Given I access to login Sauce Labs site
    When I input valid credential on Sauce Labs login page
    Then I can login successfully

  Scenario Outline: Run login with scenario outline
    Given I access to login Sauce Labs site
    When I input <username_value> and <password_value> on Sauce Labs login page
    Then I can login successfully
    Examples:
      | username_value          | password_value |
      | standard_user           | secret_sauce   |
      | performance_glitch_user | secret_sauce   |

