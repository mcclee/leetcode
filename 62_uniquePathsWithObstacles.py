class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        if len(obstacleGrid) == 1 and 1 in obstacleGrid[0]:
            return 0
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        a = []
        for i in range(m):
            if obstacleGrid[0][i] == 1:
                a = a + [0 for j in range(i, m)]
                break
            a.append(1)
        for i in range(1, n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    a[j] = 0
                else:
                    if j == 0:
                        a[j] = a[j]
                    else:
                        a[j] = a[j - 1] + a[j]
        print( a[-1])

if __name__ == '__main__':
    s = Solution()
    a = [[1],[0]]
    s.uniquePathsWithObstacles(a)