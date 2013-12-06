#!python
#encoding=utf8

import unittest
import board
import widget

class Pawn(widget.Widget):
    def __init__(self, b, x, y, team):
        super(Pawn, self).__init__(b, x, y, team)

    def IsMovingComplyRules(self, to_x, to_y):
        if self.team == 1:  # 1队在上方
            if self.y <= 5: # 没过河
                if to_x == self.x and to_y - self.y == 1:
                    # 只能向前走
                    return True
                else:
                    return False
            else: # 过河了
                if ((to_x - self.x == 1 or to_x - self.x == -1) and (to_y == self.y)) or \
                        (to_x == self.x and to_y - self.y == 1):
                    return True
                else:
                    return False
        elif self.team == 2:
            if self.y >= 6: # 没过河
                if to_x == self.x and to_y - self.y == -1:
                    # 只能向前走
                    return True
                else:
                    return False
            else: # 过河了
                if ((to_x - self.x == 1 or to_x - self.x == -1) and (to_y == self.y)) or \
                        (to_x == self.x and to_y - self.y == -1):
                    return True
                else:
                    return False

        return False

    def __repr__(self):
        return '<Pawn>'


class TestPawn(unittest.TestCase):
    def setUp(self):
        '''
        初始化工作
        '''
        b = board.Board()
        self.p = Pawn(b, 1, 1, 1)

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

