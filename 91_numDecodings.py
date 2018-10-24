from collections import deque


class Solution:

    def __init__(self):
        self.dic2 = {}

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = deque(s)
        return self.decode(a)

    def decode(self, s):
        if not s:
            return 1
        q = len(s)
        if q == 1:
            return self.checkit(s[0])
        elif q >= 2:
            if q in self.dic2:
                return self.dic2[q]
            else:
                one = s.popleft()
                q1 = self.checkit(one) * self.decode(s)
                two = s.popleft()
                q2 = self.checkit(one + two) * self.decode(s)
                s.appendleft(two)
                s.appendleft(one)
                self.dic2[q] = q1 + q2
                return q1 + q2

    def checkit(self, string):
        if 0 < int(string) < 27:
            return 1
        else:
            return 0


if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings("01"))
    