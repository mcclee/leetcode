import time


class Solution:
    def canJump(self, nums):
        if not nums or len(nums) == 1:
            return True
        vic = len(nums) - 1
        for i in reversed(range(len(nums) - 1)):
            if i + nums[i] >= vic:
                vic = i
        return vic == 0


if __name__ == '__main__':
    s = Solution()
    a = [3,2,1,0,4]
    print(len(a))
    c = time.time()
    print(s.canJump(a))
    d = time.time()
    print(d - c)

