class Solution:

    def __init__(self):
        self.dic = {}
        self.st = []

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        for i in nums:
            self.st.append(str(i))
        l = len(self.st)
        lis1 = [[self.st[0]]]
        self.dic[self.st[0]] = 1
        i = 1
        while i < l:
            lis1 = self.genper(lis1, i)
            i += 1
        new = []
        for i in lis1:
            sn = []
            for j in i:
                sn.append(int(j))
            new.append(sn)
        return new

    def genper(self, lis, i):
        newlist = []
        waitforappend = self.st[i]
        l = len(lis[0])
        for st in lis:
            for cha in range(l + 1):
                nst = st[:cha] + [waitforappend] + st[cha:]
                if self.checkif(nst):
                    newlist.append(nst)
        return newlist

    def checkif(self, list):
        check = ''
        for i in list:
            check = check + i
        if check not in self.dic:
            self.dic[check] = 1
            return True
        else:
            return False

