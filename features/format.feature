Feature: Format
  As a DevOps
  I want to specify the format
  so that I can combine the tool with other tools

  Scenario: CSV
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
          image: one:2
      """
    When I run `bin/compose_diff --versions --format=csv A.yml B.yml`
    Then it should pass with exactly:
      """
      Name;Version
      one;2 (1)
      """

  Scenario: Markdown
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
          image: one:2
      """
    When I run `bin/compose_diff --versions --format=markdown A.yml B.yml`
    Then it should pass with exactly:
      """
      | Name | Version |
      | - | - |
      | one | 2 (1) |
      """
