class Solution:
    def __init__(self):
        self.dic = {0:1, 1:1, 2:2}
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        q = n//2
        p = n - 2 * q
        return self.recur(q)
    
    def recur(self, n):
        if n in self.dic:
            return self.dic[n]
        ans = 0
        for i in range(1, n+1):
            a = self.recur(i - 1)
            b = self.recur(n - i)
            ans += (a * b)
        if n not in self.dic:
            self.dic[n] = ans
        return ans

if __name__ == '__main__':
    s = Solution()
    s.numTrees(3)
    