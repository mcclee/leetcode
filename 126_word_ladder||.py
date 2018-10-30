import copy
import time


class Solution:

    def __init__(self):
        self.l = 0
        self.wordlength = 0
        self.input = []
        self.output = []
        self.epool = {}
        self.alp = [chr(i) for i in range(97, 123)]
        self.ipool = None
        self.opool = None
        self.heads = []
        self.ends = []

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        ans = []
        self.ipool = self.opool = set(wordList)
        if endWord not in self.opool:
            return ans
        self.l = len(wordList)
        self.wordlength = len(beginWord)
        minsteps = self.fd(beginWord, endWord)
        self.input.append({beginWord})
        self.output.append({endWord})
        step = 1
        while True:
            now = set()
            if len(self.opool) <= len(self.ipool):
                curlist = self.input
                nextlist = self.output
                cpool = self.ipool
            else:
                curlist = self.output
                nextlist = self.input
                cpool = self.opool
            for j in curlist[-1]:
                if j not in self.epool:
                    self.epool[j] = self.findonedif(j, cpool)
                now = now | self.epool[j]
            step += 1
            if step >= minsteps:
                i = len(nextlist) - 1
                nodes = nextlist[i] & now
                if nodes:
                    if len(self.opool) <= len(self.ipool):
                        hindex = len(curlist) - 1
                        eindex = i - 1
                        headlist = curlist
                        endlist = nextlist
                    else:
                        hindex = i - 1
                        eindex = len(curlist) - 1
                        headlist = nextlist
                        endlist = curlist
                    for node in nodes:
                        if node == endWord or node == beginWord:
                            return [[beginWord, endWord]]
                        self.retrievelist([node], hindex, headlist, 'h')
                        self.retrievelist([node], eindex, endlist, 'e')
                        for begin in self.heads:
                            for end in self.ends:
                                ans.append(self.combine(begin, end, beginWord, endWord))
                        self.heads = []
                        self.ends = []
                if len(self.input) >= 2:
                    if self.input[-1] == self.input[-2]:
                        return ans
                if len(self.output) >= 2:
                    if self.output[-1] == self.output[-2]:
                        return ans
                if ans:
                    return ans
            if len(self.opool) <= len(self.ipool):
                self.ipool = cpool - now
            else:
                self.opool = cpool - now
            curlist.append(now)

    def findonedif(self, word, pool):
        ans = set()
        for i in range(self.wordlength):
            cb = word[:i]
            ca = word[i + 1:]
            cletter = word[i]
            for j in self.alp:
                if j != cletter:
                    cword = cb + j + ca
                    if cword in pool:
                        ans.add(cword)
        return ans

    def sumlist(self, l1):
        sums = 0
        for i in l1:
            sums += len(i)
        return sums

    def fd(self, word1, word2):
        count = 0
        for i in range(self.wordlength):
            if word1[i] != word2[i]:
                count += 1
        return count

    def retrievelist(self, nodelist, index, pool, hoe):
        if index <= 0:
            nowlist = copy.deepcopy(nodelist)
            if hoe == 'h':
                self.heads.append(nowlist)
            else:
                self.ends.append(nowlist)
        else:
            curword = nodelist[-1]
            for i in pool[index]:
                if curword in self.epool[i]:
                    nodelist.append(i)
                    self.retrievelist(nodelist, index - 1, pool, hoe)
                    nodelist.pop()

    def combine(self, begin, end, head, tail):
        newbegin = copy.deepcopy(begin)
        newend = copy.deepcopy(end)
        newbegin.append(head)
        newbegin.reverse()
        newbegin.pop()
        newend.append(tail)
        return newbegin + newend


if __name__ == '__main__':
    s = Solution()
    t1 = time.time()
    a = ["ted","tex","red","tax","tad","den","rex","pee"]
    print(s.findLadders("red", "tax", a))
    t2 = time.time()
    print(t2 - t1)