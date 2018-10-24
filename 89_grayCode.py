class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        dic = [0, 1]
        if n == 0:
            return [0]
        for i in range(1, n):
            c = pow(2, i)
            q = [j + c for j in dic]
            q.reverse()
            dic = dic + q
        return dic


if __name__ == '__main__':
    s = Solution()
    c = s.grayCode(3)
    for i in c:
        print(bin(i))