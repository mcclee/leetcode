class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        breakpoint = -1
        l = len(nums)
        if l == 0:
            return -1
        if l == 1 and nums[0] == target:
            return 0
        st = nums[0]
        if st > target:
            i = l - 1
            while i > 0:
                if nums[i] == target:
                    return i
                if i - 1 >= 0 and nums[i] < nums[i - 1]:
                    break
                i -= 1
        else:
            i = 0
            while i < l:
                if nums[i] == target:
                    return i
                if i + 1 < l and nums[i] > nums[i + 1]:
                    break
                i += 1
        return -1

if __name__ == '__main__':
    a = [1,3]
    s = Solution()
    print(s.search(a, 3))