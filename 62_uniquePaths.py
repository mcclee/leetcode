class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        a = [1 for i in range(m)]
        for i in range(n-1):
            for j in range(m):
                if j == 0:
                    a[j] = 1
                else:
                    a[j] = a[j - 1] + a[j]
        return a[-1]


if __name__ == '__main__':
    s = Solution()
    s.uniquePaths(3, 2)