# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        m = TreeNode(None)
        Em = 0
        if root:
            pre = [root]
            Em = 1
            while Em:
                Em = 0
                ans.append([i.val for i in pre])
                new = []
                for i in pre:
                    if i.left:
                        Em = 1
                        new.append(i.left)
                    if i.right:
                        Em = 1
                        new.append(i.right)
                pre = new
        return ans
        
        

