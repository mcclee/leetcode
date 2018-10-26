class Solution:
    def __init__(self):
        self.num = set('1234567890')

    def myAtoi(self, string):
        """
        :type str: str
        :rtype: int
        """
        begin = False
        count = 0
        start = -1
        PorN = 'P'
        allspace = True
        l = len(string)
        for i in range(l):
            if string[i] == ' ' and allspace is False:
                break
            if not (string[i].isalpha() or string[i].isdigit() or  string[i] == ' '):
                break
            if string[i] != ' ':
                allspace = False
            if self.checknum(string[i]):
                if begin is False:
                    begin = True
                    start = i
                    count += 1
                else:
                    count += 1
            elif begin is False:
                pass
            else:
                break
        if start == -1:
            i = 0
        else:
            if start - 1 >= 0:
                if string[start-1] == '.':
                    i = 0
                    return i
                if string[start-1] == '-':
                    if start - 2 >= 0 and (string[start-2] == '+' or string[start-2] == '-'):
                        i = 0
                        return i
                    else:
                        PorN = 'N'
                if start - 2 >= 0 and (string[start - 2:start] == '-+' or string[start - 2:start] == '++'):
                    i = 0
                    return i

            if PorN == 'P':
                i = int(string[start:start + count])
                if i > 2147483647:
                    i = 2147483647
            else:
                i = int(string[start:start + count]) * -1
                if i < -2147483648:
                    i = -2147483648
        return i

    def checknum(self, s):
        return set(s) | self.num == self.num

