#!python
#encoding=utf8

import unittest
import board

class Widget(object):
    def __init__(self, b, x, y, team):
        self.board = b
        self.x = x
        self.y = y
        self.team = team

    def IsMovingComplyRules(self, to_x, to_y):
        return False

    def __repr__(self):
        return '<Widget>'


class TestWidget(unittest.TestCase):
    def setUp(self):
        '''
        初始化工作
        '''
        b = board.Board()
        self.w = Widget(b, 1, 1, 1)

    def tearDown(self):
        '''
        退出清理工作
        '''
        pass

    def testMove(self):
        '''
        测试用例，必须以test开头
        '''
        pass

if __name__ == '__main__':
    unittest.main()
