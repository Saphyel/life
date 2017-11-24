#!/usr/bin/env python


class Universe(object):
    def __init__(self):
        self.cells = []

    def add_cell(self, cell):
        self.cells.append(cell)
        return self

    def count_neighbours(self):
        for actual in range(len(self.cells)):
            count = 0
            for next in range(len(self.cells)):
                if self.cells[actual].is_a_neighbour(self.cells[next].get_pos()):
                    count = count + 1
            self.cells[actual].set_neighbours(count - 1).validate()
        return self

    def get_cells(self):
        return self.cells
