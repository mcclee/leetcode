class Solution:

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        index = 0
        maxs = 0
        l = len(s)
        em = True
        finallen = 1
        for i in range(l):
            j = 1
            while i - j >= 0 and i + j < l:
                if s[i-j] == s[i+j]:
                    j += 1
                else:
                    break
            if 2 * j - 1 > finallen:
                finallen = 2 * j - 1
                index = i
                maxs = j - 1
                em = True
        for i in range(l):
            if i + 1 < l:
                if s[i] == s[i+1]:
                    j = 1
                    while i - j >= 0 and i + 1 + j < l:
                        if s[i - j] == s[i + j + 1]:
                            j += 1
                        else:
                            break
                    if 2*j > finallen:
                        finallen = 2*j
                        index = (i, i+1)
                        maxs = j - 1
                        em = False
        if em is True:
            return s[index-maxs: index+maxs + 1]

        else:
            return s[index[0] - maxs: index[1] + maxs + 1]

