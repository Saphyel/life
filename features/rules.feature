Feature: Descrives the behaviour of the rules
    
Scenario: The 1st rule says that a cell with less than 2 neighbours dies
    Given a universe with only 2 cells
    Then the cell 1 is dead

Scenario: The 2nd rule says that a cell with 2 neighbours will survive
    Given a universe with only 3 cells
    Then the cell 1 is alive

Scenario: The 3rd rule says that a cell with more than 3 neighbours will die
    Given a universe with a block of 4 x 4 cells
    Then the cell 2 is dead

Scenario: The 4th rule says that a cell with 3 neighbours will resurect
    Given a universe with only 2 cells
    When you add more cells
    Then the cell 1 is alive
