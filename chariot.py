#!python
#encoding=utf8

import unittest
import board
import widget

class Chariot(widget.Widget):
    def __init__(self, b, x, y, team):
        super(Chariot, self).__init__(b, x, y, team)

    def IsMovingComplyRules(self, to_x, to_y):
        b = self.board
        if to_x == self.x:
            for inter_y in range(self.y, to_y + 1):
                if b.HasWidgetOn(self.x, inter_y) == True:
                    return False
            return True

        elif to_y == self.y:
            for inter_x in range(self.x, to_x + 1):
                if b.HasWidgetOn(inter_x, self.y) == True:
                    return False
            return True

        return False

    def __repr__(self):
        return '<Chariot>'
