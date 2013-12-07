#!python
#encoding=utf8

import unittest

class Board(object):
    def __init__(self):
        self.living_widgets = []
        self.max_x = 9  # 1 - 9
        self.max_y = 10 # 1 - 10
        self.__InitEmptyBoard()

    def IsInsideChessboard(self, x, y):
        '''
        x，y的坐标起点都是1，遵循象棋棋谱
        '''
        if x >= 1 and x <= self.max_x \
                and y >= 1 and y <= self.max_y:
            return True
        else:
            return False

    def IsInsidePalace(self, x, y):
        if x >= 4 and x <= 6 \
                and ((y >= 8 and y <= 10) or (y >= 1 and y <= 3)):
            return True
        return False
           
    def IsInSameTeam(self, widget1, widget2):
        return widget1.team == widget2.team

    def __InitEmptyBoard(self):
        self.chessboard = []
        for y in range(0, self.max_y+1):
            self.chessboard.append([])
        for y in range(0, self.max_y+1):
            for x in range(0, self.max_x+1):
                self.chessboard[y].append(None)

    def SetUp(self):
        # 1队在上方，2队在下方
        # 兵
        for x in range(1, self.max_x+1, 2):
            y = 4
            self.__SetWidgetOn(pawn.Pawn(self, x, y, 1), x, y)
            y = 7
            self.__SetWidgetOn(pawn.Pawn(self, x, y, 2), x, y)
        # 炮
        for x in [2, 8]:
            y = 3
            self.__SetWidgetOn(cannon.Cannon(self, x, y, 1), x, y)
            y = 8
            self.__SetWidgetOn(cannon.Cannon(self, x, y, 2), x, y)
        # 车
        for x in [1, 9]:
            y = 1
            self.__SetWidgetOn(chariot.Chariot(self, x, y, 1), x, y)
            y = 10
            self.__SetWidgetOn(chariot.Chariot(self, x, y, 2), x, y)
        # 马
        for x in [2, 8]:
            y = 1
            self.__SetWidgetOn(horse.Horse(self, x, y, 1), x, y)
            y = 10
            self.__SetWidgetOn(horse.Horse(self, x, y, 2), x, y)
        # 象
        for x in [3, 7]:
            y = 1
            self.__SetWidgetOn(bishop.Bishop(self, x, y, 1), x, y)
            y = 10
            self.__SetWidgetOn(bishop.Bishop(self, x, y, 2), x, y)
        # 士
        for x in [4, 6]:
            y = 1
            self.__SetWidgetOn(guard.Guard(self, x, y, 1), x, y)
            y = 10
            self.__SetWidgetOn(guard.Guard(self, x, y, 2), x, y)
        # 帅
        for x in [5]:
            y = 1
            self.__SetWidgetOn(king.King(self, x, y, 1), x, y)
            y = 10
            self.__SetWidgetOn(king.King(self, x, y, 2), x, y)
        
        
    def __repr__(self):
        info = ''
        for y in range(1, self.max_y+1):
            for x in range(1, self.max_x+1):
                #print x,y, self.__GetWidgetOn(x,y)
                info += repr(self.__GetWidgetOn(x, y)) + '\t'
            info += '\n'
        return info

    def MoveWidgetTo(self, x, y, to_x, to_y):
        if x == to_x and y == to_y:
            return False
        if self.IsInsideChessboard(x, y) == False:
            return False
        source_widget = self.__GetWidgetOn(x, y)
        if source_widget == None:
            return False
        if self.IsInsideChessboard(to_x, to_y) == False:
            return False

        taget_widget = self.__GetWidgetOn(to_x, to_y)
        if taget_widget != None:
            if self.IsInSameTeam(source_widget, taget_widget) == False:
                # 不能吃自己的棋子
                return False

        if source_widget.IsMovingComplyRules(to_x, to_y) == False:
            return False
        source_widget.x = to_x
        source_widget.y = to_y
        self.__RemoveWidgetOn(x, y)
        self.__SetWidgetOn(source_widget, x, y)

    def HasWidgetOn(self, x, y):
        return self.chessboard[y][x] != None

    def __GetWidgetOn(self, x, y):
        return self.chessboard[y][x]

    def __SetWidgetOn(self, widget_item, x, y):
        self.chessboard[y][x] = widget_item

    def __RemoveWidgetOn(self, x, y):
        self.chessboard[y][x] = None



class TestBoard(unittest.TestCase):
    def setUp(self):
        '''
        初始化工作
        '''
        self.b = Board()

    def tearDown(self):
        '''
        退出清理工作
        '''
        pass

    def testIsInsideChessboard(self):
        '''
        测试用例，必须以test开头
        '''
        for x in range(1, 9):
            for y in range(1, 10):
                self.assertTrue(self.b.IsInsideChessboard(x,y), '%i,%i'%(x,y))

        for x in range(1, 9):
            for y in [-1, 0, 11, 100]:
                self.assertFalse(self.b.IsInsideChessboard(x,y), '%i,%i'%(x,y))

        for x in [-1, 0, 10, 100]:
            for y in range(1, 10):
                self.assertFalse(self.b.IsInsideChessboard(x,y), '%i,%i'%(x,y))

    def testPrint(self):
        print self.b

    def testSetUp(self):
        self.b.SetUp()
        print self.b

    def testMovePawn(self):
        self.b.SetUp()
        print self.b

if __name__ == '__main__':
    import widget
    import pawn, cannon, chariot, horse, bishop, guard, king
    unittest.main()


