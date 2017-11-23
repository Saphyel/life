#!/usr/bin/env python


class Cell(object):
    def __init__(self, pos_x=0, pos_y=0):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.alive = True
        self.neighbours = 0

    def get_pos(self):
        return [self.pos_x, self.pos_y]

    def is_a_neighbour(self, pos):
        if (self.pos_x == pos[0] + 1 or self.pos_x == pos[0] - 1 or self.pos_x == pos[0]) and (self.pos_y == pos[1] + 1 or self.pos_y == pos[1] - 1 or self.pos_y == pos[1]):
            return True
        return False

    def is_alive(self):
        return self.alive

    def set_neighbours(self, neighbours):
        self.neighbours = neighbours
        return self

    def validate(self):
        if self.alive:
            self.rules_alive()
        else:
            self.rules_dead()
        return self

    def rules_alive(self):
        if self.neighbours < 2 or self.neighbours > 3:
            self.alive = False
        return self

    def rules_dead(self):
        if self.neighbours == 3:
            self.alive = True
        return self
