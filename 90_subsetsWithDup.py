class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def g(nums):
            if not nums:
                return [()]
            t = g(nums[1:])
            return list(set([(nums[0],)+sub for sub in t] + t))
        nums.sort()
        return g(nums) if nums else []
    

if __name__ == '__main__':
    a = [3, 5, 0, 4, 3]
    s = Solution()
    print(s.subsetsWithDup(a))

        
