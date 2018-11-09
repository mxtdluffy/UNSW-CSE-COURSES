'''
horse rides sun problem
use backtracking algorithm
author:ztp
create at:2015/1/19 15:06
'''
 
class HorseRides:
    def __init__(self, n, m, x, y):
        self.row = n
        self.column = m
        self.startx = x
        self.starty = y
        self.chessboard = [[0]*self.column for r in range(self.row+1)]
        self.sunx = [1, 1, 2, 2,-1,-1,-2,-2]
        self.suny = [2,-2, 1,-1, 2,-2, 1,-1]
        self.chessboard[self.startx][self.starty] = 1;
        self.count = 0;
    def check(self, x, y):
        if x >= self.row or y >= self.column or x < 0 or y < 0 or self.chessboard[x][y] != 0:
            return 0;
        return 1;
    def ride(self, x, y, step):
        for i in range(8):
            xx = x + self.sunx[i]
            yy = y + self.suny[i]
            if self.check(xx, yy) == 1:
                self.chessboard[xx][yy] = step;
                if step == self.row * self.column:
                    self.output();
                else:
                    self.ride(xx, yy, step+1)
                self.chessboard[xx][yy] = 0
    def output(self):
        self.count = self.count + 1
        print ("count = %d" % self.count)
        for i in range(self.row):
            print(self.chessboard[i])
    def getCount(self):
        return self.count
 
 
if __name__ == "__main__":
    horseride = HorseRides(9,9,0,0)
    horseride.ride(0, 0, 2)
    print ("total path: %d" % horseride.getCount())
