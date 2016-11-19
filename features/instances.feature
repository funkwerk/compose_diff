Feature: Instances
  As an Operations Manager
  I want to see how many instances are deployed
  so that I know where the scalling happens

  Scenario: Instances
    Given a file named "A.yml" with:
      """
      version: "2"
      services:
        one:
          image: one:1
      """
    And a file named "B.yml" with:
      """
      version: "2"
      services:
        one:
          image: one:1
        one_2:
          image: one:1
      """
    When I run `bin/compose_diff --instances A.yml B.yml`
    Then it should pass with exactly:
      """
      | Name | Instances |
      | - | - |
      | one | 2 (1) |
      """
