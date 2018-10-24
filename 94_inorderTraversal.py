# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
            self.ans = []

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.inorder(root)
        return self.ans
    
    def inorder(self, node):
        if node:
            if node.left is None and node.right is None:
                self.ans.append(node.val)
                return True
            self.inorder(node.left)
            self.ans.append(node.val)
            self.inorder(node.right)
        else:
            return True