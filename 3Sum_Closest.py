class Solution1:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        tar = target
        l = len(nums)
        nums.sort()
        di = {}
        for i in nums:
            if i not in di:
                di[i] = 1
            else:
                di[i] += 1
        if l < 3:
            return 0
        elif l == 3:
            return sum(nums)
        count = 0
        while True:
            i = 0
            while i < l:
                j = i + 1
                while j < l:
                    c = nums[i] + nums[j]
                    c = tar - c
                    if c in di:
                        if nums[i] != nums[j] and nums[j] != c and nums[i] != c:
                            return tar
                        elif nums[i] == nums[j] and nums[j] != c and di[nums[i]] >= 2:
                            return tar
                        elif nums[j] == c and nums[i] != nums[j] and di[nums[j]] >= 2:
                            return tar
                        elif nums[j] == c == nums[i] and di[nums[i]] >= 3:
                            return tar
                        elif nums[i] == c and nums[i] != nums[j] and di[nums[i]] >= 2:
                            return tar
                    j += 1
                i += 1
            if count > 0:
                count = count + 1
            else:
                count = count - 1
            count *= (-1)
            tar += count


if __name__ == '__main__':
    a = [13, 2,0,-14,-20,19,8,-5,-13,-3,20 ,15,20,5,13,14,-17,-7,12,-6,0,20,-19,-1,-15,-2,8,-2,-9,13,0,-3,-18,-9,-9,-19,17,-14,-19,-4,-16,2,0,9,5,-7,-4,20,18,9,0,12,-1,10,-17,-11,16,-13,-14,-3,0,2,-18,2,8,20,-15,3,-13,-12,-2,-19,11,11,-10,1,1,-10,-2,12,0,17,-19,-7,8,-19,-17,5,-5,-10,8,0,-12,4,19,2,0,12,14,-9,15,7,0,-16,-5,16,-12,0,2,-16,14,18,12,13,5,0,5,6]

    s = Solution1()
    print(s.threeSumClosest(a, -59))
