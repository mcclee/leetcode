class Solution:
    def __init__(self):
        self.str = 'abcdefghijklmnopqrstuvwxyz'
        self.dic = {}
        for i in range(2, 10):
            if i <= 6:
                self.dic[str(i)] = self.str[3 * (i - 2): 3 * (i - 2) + 3]
        self.dic['7'] = 'pqrs'
        self.dic['8'] = 'tuv'
        self.dic['9'] = 'wxyz'

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ref = ''
        for i in digits:
            if i in self.dic:
                ref = ref + i
        l = len(ref)
        if ref == '':
            return []
        num= 1
        re = []
        for i in self.dic[ref[0]]:
            re.append(i)
        while num < l:
            for i in ref[num]:
                sec = []
                for j in self.dic[i]:
                    sec2 = [dig + j for dig in re]
                    for p in sec2:
                        sec.append(p)
                re = sec
            num += 1
        return re


if __name__ == '__main__':
    k = '23'
    a = Solution()
    print(a.letterCombinations(k))