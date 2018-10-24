class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        n = len(nums)
        for k in range(n + 1):
            c_list = []
            c = []
            self.search(0, c_list, c, n, k, nums)
            ans = ans + c_list
        return ans

    def search(self, i, c_list, c, n, k, nums):
        if k == 0:
            c_list.append([x for x in c])
            return

        while i < n - k + 1:
            c.append(nums[i])
            self.search(i + 1, c_list, c, n, k - 1, nums)
            c.pop()
            i += 1


if __name__ == '__main__':
    a = [1,2,3]
    s = Solution()
    s.subsets(a)