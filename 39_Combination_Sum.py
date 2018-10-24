import copy
class Solution:
    def __init__(self):
        self.ans = []

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        if candidates[0] > target:
            return []
        self.getacandidates(candidates, target, [], 0)
        return self.ans

    def getacandidates(self, candidates, target, ingd, begin):
        for i in candidates[begin:]:
            if target == i + sum(ingd):
                c = copy.deepcopy(ingd)
                c.append(i)
                self.ans.append(c)
                return True
            if target > i + sum(ingd):
                c = copy.deepcopy(ingd)
                c.append(i)
                self.getacandidates(candidates, target, c, begin)
            if target < i + sum(ingd):
                return False
            begin += 1
        return True


if __name__ == '__main__':
    s = Solution()
    a = [2,3,5]
    s.combinationSum(a, 8)
    print(s.ans)
