#!/usr/bin/env python
from life.universe import Universe
from life.cell import Cell


def test_add_and_get_cell():
    universe = Universe()
    cell = Cell(1, 1)
    universe.add_cell(cell)
    assert universe.get_cells() == [cell]
