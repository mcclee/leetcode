class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if nums:
            if len(nums) >= 2:
                s1 = len(nums)//2
                if nums[0] <= target <= nums[-1]:
                    if self.search(nums[:s1], target) or self.search(nums[s1:], target):
                        return True
                else:
                    if nums[-1] <= nums[0]:
                        if self.search(nums[:s1], target) or self.search(nums[s1:], target):
                            return True
            else:
                return nums[0] == target
        return False


if __name__ == '__main__':
    nums = [1,2,1]

    target = 2
    s = Solution()
    print(s.search(nums, target))