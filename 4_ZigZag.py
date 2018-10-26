class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        l = len(s)
        if numRows * 2 - 2 == 0:
            return s
        lo = int(l / (numRows * 2 - 2))
        rem = l % (numRows * 2 - 2)
        if rem <= numRows:
            lo = 1 + (numRows - 1) * lo
        else:
            lo = (numRows - 1) * lo + 1 + rem - numRows
        sl = self.cre(lo, numRows)
        chang = 0
        kuan = 0
        for i in s:
            sl[kuan][chang] = i
            if kuan + 1 == numRows:
                kuan -= 1
                chang += 1
            elif kuan - 1 >= 0 and sl[kuan - 1][chang] == '':
                kuan -= 1
                chang += 1
            else:
                kuan += 1
        string = ''
        for i in sl:
            for j in i:
                if j != '':
                    string = string + j
        return string

    def cre(self, l, w):
        lis = []
        for i in range(w):
            a = []
            for j in range(l):
                a.append('')
            lis.append(a)
        return lis
