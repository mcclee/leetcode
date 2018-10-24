class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        ans = [-1, -1]
        if l == 0:
            return [-1, -1]
        if l == 1 and nums[0] == target:
            return [0, 0]
        st = nums[0]
        if st > target:
            i = l - 1
            start = 0
            org = -1
            while i > 0:
                if nums[i] == target:
                    if start == 0:
                        org = i
                    start += 1
                    if i - 1 >= 0 and nums[i - 1] != target:
                        ans = [i, org]
                    if i == 0:
                        ans = [i, org]
                if i - 1 >= 0 and nums[i] < nums[i - 1]:
                    break
                i -= 1
        else:
            i = 0
            start = 0
            org = -1
            while i < l:
                if nums[i] == target:
                    if start == 0:
                        org = i
                    start += 1
                    if i + 1 < l and nums[i + 1] != target:
                        ans = [org, i]
                    if i + 1 == l:
                        ans = [org, i]
                if i + 1 < l and nums[i] > nums[i + 1]:
                    break
                i += 1
        return ans


if __name__ == '__main__':
    a = [5,7,7,8,8,8]
    s = Solution()
    print(s.searchRange(a, 8))
