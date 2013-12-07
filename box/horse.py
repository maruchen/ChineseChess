#!python
#encoding=utf8

import unittest
import board
import widget

class Horse(widget.Widget):
    def __init__(self, b, x, y, team):
        super(Horse, self).__init__(b, x, y, team)

    def IsMovingComplyRules(self, to_x, to_y):
        b = self.board
        if (to_x - self.x == 2) and  \
                (to_y - self.y == 1 or to_y - self.y == -1) and \
                b.HasWidgetOn(self.x + 1, self.y) == False:
            return True
        if (to_x - self.x == -2) and  \
                (to_y - self.y == 1 or to_y - self.y == -1) and \
                b.HasWidgetOn(self.x - 1, self.y) == False:
            return True
        if (to_y - self.y == 2) and \
                (to_x - self.x == 1 or to_x - self.x == -1) and \
                b.HasWidgetOn(self.x, self.y + 1) == False:
            return True
        if (to_y - self.y == -2) and \
                (to_x - self.x == 1 or to_x - self.x == -1) and \
                b.HasWidgetOn(self.x, self.y - 1) == False:
            return True

        return False

    def __repr__(self):
        return '<Horse>'

class TestHorse(unittest.TestCase):
    def setUp(self):
        '''
        初始化工作
        '''
        pass
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






