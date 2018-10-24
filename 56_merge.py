# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key= lambda x: x.start)
        l = len(intervals)
        ans = []
        if not intervals:
            return []
        newInterval = intervals[0]
        for i in range(1, l):
            if (newInterval.start - intervals[i].end) * (newInterval.end - intervals[i].start) <= 0:
                newInterval.start = min(newInterval.start, intervals[i].start)
                newInterval.end = max(newInterval.end, intervals[i].end)
            else:
                ans.append(newInterval)
                newInterval = intervals[i]
        ans.append(newInterval)
        for i in ans:
            print(i.start, i.end)


if __name__ == '__main__':
    b = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
    a = []
    for i in b:
        k = Interval(i[0], i[1])
        a.append(k)
    s =Solution()
    s.merge(a)

