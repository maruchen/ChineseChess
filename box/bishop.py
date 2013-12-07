#!python
#encoding=utf8

import unittest
import board
import widget

class Bishop(widget.Widget):
    def __init__(self, b, x, y, team):
        super(Bishop, self).__init__(b, x, y, team)

    def IsMovingComplyRules(self, to_x, to_y):
        b = self.board
        if self.team == 1: # 上方
            if to_y > 5:
                return False
        if self.team == 2: # 下方
            if to_y < 6:
                return False

        if ((to_x - self.x) == 2 and (to_y - self.y) == 2) or \
           ((to_x - self.x) == 2 and (to_y - self.y) == -2) or \
           ((to_x - self.x) == -2 and (to_y - self.y) == 2) or \
           ((to_x - self.x) == -2 and (to_y - self.y) == -2):
            return True

        return False

    def __repr__(self):
        return '<Bishop>'

