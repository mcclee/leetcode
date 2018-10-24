class Solution:

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        b = board
        l = len(b)
        r = len(b[0])
        dic = {}
        for i in range(l):
            for j in range(r):
                if b[i][j] != '.':
                    if b[i][j] not in dic:
                        dic[b[i][j]] = [[i, j]]
                    else:
                        dic[b[i][j]].append([i, j])
        print(dic)
        for i in dic:
            if len(dic[i]) > 1:
                count = 0
                while count < len(dic[i]) - 1:
                    cr = count + 1
                    while cr < len(dic[i]):
                        if self.sudoornot(dic[i][count], dic[i][cr]) is False:
                            return False
                        cr += 1
                    count += 1

        return True

    def sudoornot(self, num1, num2):
        if num1[0] == num2[0] or num1[1] == num2[1]:
            return False
        elif int(num1[0]/3) == int(num2[0]/3) and int(num1[1]/3) == int(num2[1]/3):
            return False
        else:
            return True


if __name__ == '__main__':
    a = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    s = Solution()
    print(s.isValidSudoku(a))
