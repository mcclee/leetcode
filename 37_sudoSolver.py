import random
from operator import itemgetter
import copy


class Solution:
    def __init__(self):
        self.newdic = {}
        self.board = None
        self.ele = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in self.ele:
            self.newdic[i] = []

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        firstrow = -1
        firstcol = -1
        count = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    self.newdic[board[i][j]].append([i, j])
                else:
                    if count == 0:
                        firstrow, firstcol = i, j
                        count += 1

        for i in self.ele:
            if i not in self.newdic or len(self.newdic[i]) != 9:
                ans = self.backtracking(board, firstrow, firstcol, i)
                if ans is True:
                    break
        print(self.board)

    def backtracking(self, board, currow, curcol, curnum):
        row = currow
        col = curcol
        board[currow][curcol] = curnum
        self.newdic[curnum].append([currow, curcol])
        if self.calconflict(currow, curcol):
            nextrow, nextcol = self.findnext(row, col)
            if nextrow == -1 and nextcol == -1:
                return True
            else:
                for i in self.ele:
                    if len(self.newdic[i]) < 9:
                        if self.backtracking(board, nextrow, nextcol, i) is True:
                            return True
        board[currow][curcol] = '.'
        self.newdic[curnum].remove([currow, curcol])
        return False

    def findnext(self, row, col):
        while self.board[row][col] != '.':
            if col == 8 and row == 8:
                return -1, -1
            if col == 8:
                row += 1
                col = 0
            else:
                col += 1
        return row, col

    def calconflict(self,row, col):
        if self.board[row][col] in self.newdic:
            for i in self.newdic[self.board[row][col]]:
                if i != [row, col]:
                    if self.sudoornot([row, col], i) is not True:
                        return False
        return True

    def sudoornot(self, num1, num2):
        if num1[0] == num2[0] or num1[1] == num2[1]:
            #print(num1, num2)
            return False
        elif int(num1[0]/3) == int(num2[0]/3) and int(num1[1]/3) == int(num2[1]/3):
            #print(num1, num2)
            return False
        else:
            return True


if __name__ == '__main__':
    a = [[".",".",".",".",".","7",".",".","9"],[".","4",".",".","8","1","2",".","."],[".",".",".","9",".",".",".","1","."],[".",".","5","3",".",".",".","7","2"],["2","9","3",".",".",".",".","5","."],[".",".",".",".",".","5","3",".","."],["8",".",".",".","2","3",".",".","."],["7",".",".",".","5",".",".","4","."],["5","3","1",".","7",".",".",".","."]]
    s = Solution()
    s.solveSudoku(a)

