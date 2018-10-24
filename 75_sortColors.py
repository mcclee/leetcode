class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        l = len(nums)
        i = 0
        count = 0
        while i < l:
            if nums[i] == 1:
                nums.pop(i)
                nums.append(1)
                l -= 1
            elif nums[i] == 2:
                nums.pop(i)
                count += 1
                l -= 1
            else:
                i += 1
        for i in range(count):
            nums.append(2)

        print(nums)

if __name__ == '__main__':
    a = [2,0,2,1,1,0]
    s = Solution()
    s.sortColors(a)