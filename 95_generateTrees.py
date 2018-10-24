# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        foruse = [i for i in range(1, n+1)]
        a = self.gentree(foruse, 1)
        return a

    def gentree(self, nums):
        if len(nums) == 1:
            return [TreeNode(nums[0])]
        elif not nums:
            return [None]
        if len(nums) > 1:
            ans = []
            for treenode in range(len(nums)):
                lefts = self.gentree(nums[:treenode])
                rights = self.gentree(nums[treenode + 1:])
                for i in lefts:
                    for j in rights:
                        md = TreeNode(nums[treenode])
                        md.left = i
                        md.right = j
                        ans.append(md)
            return ans


if __name__ == '__main__':
    s = Solution()
    s.generateTrees(0)


    
