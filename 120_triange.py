class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        s = [0]
        l = len(triangle)
        for i in range(l):
            currow = triangle[i]
            rowl = len(currow)
            new = []
            for j in range(rowl):
                if j == 0:
                    new.append(currow[j] + s[j])
                elif j == rowl - 1:
                    new.append(currow[j] + s[j - 1])
                else:
                    new.append(min(currow[j] + s[j], currow[j] + s[j - 1]))
            s = new
        return min(s)


if __name__ == '__main__':
    a = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
    s = Solution()
    print(s.minimumTotal(a))





