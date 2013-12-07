#!python
#encoding=utf8

import unittest
import board


def _BaseAlgorithm(current_board, my_team_widgets):
    pass

class AIBase(object):
    def __init__(self):
        pass

    def NextStep(self, current_board, current_move_team):
        '''
        修改board
        '''
        my_team_widgets = []
        for y in range(1, self.max_y+1):
            for x in range(1, self.max_x+1):
                w = current_board.__GetWidgetOn(x, y)
                if w != None and w.team == current_team:
                    my_team_widgets.append(w)


