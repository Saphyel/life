#!/usr/bin/env python
from life.cell import Cell


def test_get_pos():
    cell = Cell(1, 1)
    assert cell.get_pos() == [1, 1]


def test_is_a_neighbour():
    cell = Cell(1, 1)
    assert cell.is_a_neighbour([2, 2]) is True
    assert cell.is_a_neighbour([3, 3]) is False


def test_rules():
    cell = Cell(1, 1)
    cell.set_neighbours(2)
    cell.rules_alive()
    assert cell.is_alive() is True
    cell.set_neighbours(1)
    cell.validate()
    assert cell.is_alive() is False
    cell.set_neighbours(3)
    cell.validate()
    assert cell.is_alive() is True
