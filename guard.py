#!python
#encoding=utf8

import unittest
import board
import widget

class Guard(widget.Widget):
    def __init__(self, b, x, y, team):
        super(Guard, self).__init__(b, x, y, team)

    def IsMovingComplyRules(self, to_x, to_y):
        b = self.board
        if b.IsInsidePalace(to_x, to_y) == False:
            return False

        if ((to_x - self.x) == 1 and (to_y - self.y) == 1) or \
           ((to_x - self.x) == 1 and (to_y - self.y) == -1) or \
           ((to_x - self.x) == -1 and (to_y - self.y) == 1) or \
           ((to_x - self.x) == -1 and (to_y - self.y) == -1):
            return True

        return False

    def __repr__(self):
        return '<Guard>'

