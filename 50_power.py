class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ans = 1

        rest = abs(n)

        while rest > 0:
            anss, count = self.power(x, rest)
            rest = rest - count
            ans *= anss
            if ans > 2147483648:
                ans = 2147483648
                break

        if n > 0:
            if x < 0:
                if n % 2 == 0:
                    ans = abs(ans)
                else:
                    ans = -abs(ans)
        elif n < 0:
            if x < 0:
                if n % 2 == 0:
                    ans = 1/abs(ans)
                else:
                    ans = -1/abs(ans)
            else:
                ans = 1 / ans
        else:
            ans = 1
        print(ans)

    def power(self, x, n):
        s = x
        count = 1
        while count * 2 < abs(n):
            s *= s
            count *= 2
            if s > 2147483648:
                s = 2147483648
                break
        return s, count


if __name__ == '__main__':
    s = Solution()
    x, n = 2.00000, -2
    s.myPow(x, n)