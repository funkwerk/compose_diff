Feature: Versions
  As a Tester
  I want to see which image versions have changed
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
    When I run `bin/compose_diff --versions A.yml B.yml`
    Then it should pass with exactly:
      """
      | Name | Version |
      | - | - |
      | four | 1 (deleted) |
      | one | 1 |
      | three | 1 (new) |
      | two | 2 (1) |
      """

  Scenario: Multiple Versions for specific image
    Given a file named "A.yml" with:
      """
      version: "2"
      services:
        one:
          image: A:1
        two:
          image: A:2
      """
    And a file named "B.yml" with:
      """
      version: "2"
      services:
        one:
          image: A:2
        two:
          image: A:3
      """
    When I run `bin/compose_diff --versions A.yml B.yml`
    Then it should pass with exactly:
      """
      | Name | Version |
      | - | - |
      | A | 2, 3 (1, 2) |
      """

  Scenario: Filter
    Given a file named "A.yml" with:
      """
      version: "2"
      services:
        one:
          image: one:1
        two:
          image: two:1
      """
    And a file named "B.yml" with:
      """
      version: "2"
      services:
        one:
          image: one:2
        two:
          image: two:2
      """
    When I run `bin/compose_diff --version --filter one A.yml B.yml`
    Then it should pass with exactly:
      """
      | Name | Version |
      | - | - |
      | one | 2 (1) |
      """
