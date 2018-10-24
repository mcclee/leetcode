import time


class Solution:

    def __init__(self):
        self.ninenine = {}
        self.dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        l = len(self.dic)
        for i in range(l):
            for j in range(l):
                muti = self.getans(i, j)
                self.ninenine[self.dic[i] + '*' + self.dic[j]] = muti
                self.ninenine[self.dic[j] + '*' + self.dic[i]] = muti

    def getans(self, num1, num2):
        if num2 > num1:
            num1, num2 = num2, num1
        s = 0
        for i in range(num2):
            s += num1
        return str(s)

    def sumall(self, num1, num2):
        num1 = num1[::-1]
        num2 = num2[::-1]
        l1 = len(num1)
        l2 = len(num2)
        s = ''
        i = 0
        jin = '0'
        if l1 < l2:
            l1, l2 = l2, l1
            num1, num2 = num2, num1
        while i < l1:
            if i < l2:
                n2 = num2[i]
            else:
                n2 = '0'
            n1 = num1[i]
            plusone = jin
            jin, rest = self.getsum(n1, n2)
            jins, num = self.getsum(rest, plusone)
            if jins == '1':
                q, jin = self.getsum(jin, '1')
            s = num + s
            i += 1
        s = jin + s
        count = 0
        while count < len(s) and s[count] == '0':
            count += 1
        s = s[count:]
        return s

    def getsum(self, num1, num2):
        lo1 = self.dic.index(num1)
        lo2 = self.dic.index(num2)
        if lo1 + lo2 >= 10:
            jinwei = '1'
            rest = self.dic[lo2 + lo1 - 10]
        else:
            jinwei = '0'
            rest = self.dic[lo2 + lo1]
        return jinwei, rest

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'

        if len(num2) > len(num1):
            num1, num2 = num2, num1
        l1 = len(num1)
        l2 = len(num2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        s = []
        for i in range(0, l2):
            seg = ''
            end = ''
            j = 0
            sss = []
            while j <= l1 - 1:
                muti = self.ninenine[num1[j] + '*' + num2[i]] + end
                sss.append(muti)
                j += 1
                end = end + '0'
            ss = '0'
            if sss:
                for i in sss:
                    ss = self.sumall(ss, i)
            s.append(ss)
        rs = '0'
        if s:
            end = ''
            for i in s:
                rs = self.sumall(rs, i + end)
                end = end + '0'
        print(rs)


if __name__ == '__main__':
    s = Solution()
    a = time.time()
    s.multiply("7950730684116360645035469888615500796", "841979251126152713721537069775651940998000937338602066982")
    b = time.time()
    print(b - a)

