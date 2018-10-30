# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.ans = 0

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            self.sumall(root, 0)
            return self.ans
        else:
            return 0

    def sumall(self, node, sums):
        if node.left:
            self.sumall(node.left, sums * 10 + node.val)
        if node.right:
            self.sumall(node.right, sums * 10 + node.val)
        if not self.isitleaf(node):
            self.ans += sums * 10 + node.val

    def isitleaf(self, node):
        return node.left or node.right


if __name__ == '__main__':
    i = TreeNode(1)
    j = TreeNode(2)
    K = TreeNode(3)
    i.left = j
    i.right = K
    s = Solution()
    s.sumNumbers(i)
