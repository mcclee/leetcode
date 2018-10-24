import time


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        fuhao = True
        if dividend > 0 and divisor < 0:
            fuhao = False
        elif dividend < 0 and divisor > 0:
            fuhao = False
        divisor = abs(divisor)
        dividend = abs(dividend)
        sums = 0
        org = 0
        while dividend > 10 and dividend >= divisor:
            a, times = self.findmaxtens(dividend, divisor)
            org += times
            dividend -= a
        while dividend >= divisor:
            dividend -= divisor
            org += 1

        if fuhao:
            if org <= 2147483647:
                return org
            else:
                return 2147483647
        else:
            if org >= -2147483648:
                return 0 - org
            else:
                return -2147483648

    def findmaxtens(self, num, div):
        n = str(num)
        d = str(div)
        dis = len(n)-len(d)
        tims = '1'
        if dis > 0:
            i = 0
            while dis > i:
                d = d + '0'
                tims = tims + '0'
                i += 1
            if int(d) > num:
                d = d[:-1]
                tims = tims[:-1]
        m = int(d)
        t = int(tims)
        while m + int(d) < num:
            m += int(d)
            t += int(tims)
        return m, t

if __name__ == '__main__':
    a = -2147483648
    b = -1
    s = Solution()
    t1 = time.time()
    print(s.divide(a, b))
    print(a/b)
    t2 = time.time()
    print(t2 - t1)

