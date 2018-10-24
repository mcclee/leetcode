class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row = set()
        col = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row = row | {i}
                    col = col | {j}
        for i in range(m):
            if i in row:
                matrix[i] = [0 for i in range(n)]
            else:
                for j in range(n):
                    if j in col:
                        matrix[i][j] = 0
        print(matrix)


if __name__ == '__main__':
    s = Solution()
    a = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
    s.setZeroes(a)

