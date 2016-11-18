Feature: Images
  As a Tester
  I want to see which images have changed
  so that I know where to test especially

  Scenario: Diff Images
    Given a file named "A.yml" with:
      """
      version: "2"
      services:
        one:
          image: one:1
        two:
          image: two:1
        four:
          image: four:1
      """
    And a file named "B.yml" with:
      """
      version: "2"
      services:
        one:
          image: one:1
        two:
          image: two:2
        three:
          image: three:1
      """
    When I run `bin/compose_diff --images A.yml B.yml`
    Then it should pass with exactly:
      """
      | Name | Version |
      | - | - |
      | four | 1 (deleted) |
      | one | 1 |
      | three | 1 (new) |
      | two | 2 (1) |
      """
