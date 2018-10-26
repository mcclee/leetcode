

class Solution:
    def __init__(self):
        self.set = 0

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        x = len(s)
        j = 0
        while j < x:
            if self.checkit(s[0:(j+1)]):
                j += 1
            else:
                break
        i = 1
        while i < x:
            if i + j >= x:
                break
            while self.checkit(s[i:(i+j+1)]):
                if i+j >= x:
                    break
                j += 1
            i += 1
        maxs = j
        return maxs

    def checkit(self, string):
        return len(set(string)) == len(string)



