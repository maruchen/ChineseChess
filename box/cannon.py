#!python
#encoding=utf8

import unittest
import board
import widget

class Cannon(widget.Widget):
    def __init__(self, b, x, y, team):
        super(Cannon, self).__init__(b, x, y, team)

    def IsMovingComplyRules(self, to_x, to_y):
        b = self.board
        if to_x == self.x:
            inter_counter = 0
            for inter_y in range(self.y, to_y + 1):
                if b.HasWidgetOn(self.x, inter_y) == True:
                    inter_counter +=1
            if inter_counter == 1:
                return True
            else:
                return False

        elif to_y == self.y:
            inter_counter = 0
            for inter_x in range(self.x, to_x + 1):
                if b.HasWidgetOn(inter_x, self.y) == True:
                    inter_counter +=1
            if inter_counter == 1:
                return True
            else:
                return False

        return False

    def __repr__(self):
        return '<Cannon>'
