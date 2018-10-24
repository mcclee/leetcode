from collections import deque


class Solution:

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        i = 1
        ans = deque()
        dic = {}
        while i <= n:
            if i == 1:
                ans.append('()')
            else:
                while len(ans[0]) != 2 * i:
                    a = ans.popleft()
                    for j in range(len(a) + 1):
                        new = a[0:j] + '()' + a[j:]
                        if new not in dic:
                            dic[new] = 1
                            ans.append(new)
            i += 1
        ans2 = []
        for q in ans:
            ans2.append(q)
        return ans2


if __name__ == '__main__':
    c = 3
    s = Solution()
    print(s.generateParenthesis(c))
