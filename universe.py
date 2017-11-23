#!/usr/bin/env python
from cell import Cell


class Universe(object):
    def __init__(self):
        self.cells = []

    def add_cell(self, cell):
        self.cells.append(cell)
        return self

    def count_neighbours(self):
        for actual in self.cells:
            count = 0
            for next in self.cells:
                if self.cells[actual].is_a_neighbour(self.cells[next]):
                    count = count + 1
            self.cells[actual].set_neighbours(count - 1).validate()
        return self

