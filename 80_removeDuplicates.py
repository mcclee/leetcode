class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        cur = ''
        l = len(nums)
        i = 0
        while i < l:
            if nums[i] != cur:
                cur = nums[i]
                count = 1
            else:
                if count > 2:
                    nums.pop(i)
                    l -= 1
                else:
                    count += 1
                    i += 1



if __name__ == '__main__':
    s = Solution()
    a = [0,0,1,1,1,1,2,3,3]
    s.removeDuplicates(a)
