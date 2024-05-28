Feature: Example feature
  Scenario Outline: Addition
    Given I have the numbers <a> and <b>
    When I add the numbers
    Then the result should be <result>

    Examples:
      | a | b | result |
      | 1 | 2 | 3      |
      | 2 | 3 | 5      |
      | 5 | 5 | 10     |