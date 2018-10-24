from collections import deque
import math
import time


class Solution:

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 0:
            return []
        sdk = deque('1')
        for i in range(2, n):
            while len(sdk[0]) != i:
                s = sdk.popleft()
                for j in reversed(range(len(s) + 1)):
                    sdk.append(s[:j] + str(i) + s[j:])
        ans = sorted(list(sdk), key=lambda x: int(x))
        q = math.factorial(n - 1)
        i = k % q
        j = (k - i) / q
        s = ans[i - 1]
        return s[:-j] + str(i) + s[-j:]


if __name__ == '__main__':
    s = Solution()
    a = time.time()
    print(s.getPermutation(3, 3))
    b = time.time()
    print(b - a)


