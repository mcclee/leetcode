# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        Em = 0
        if root:
            pre = [root]
            Em = 1
            level = 0
            while Em:
                Em = 0
                a = [i.val for i in pre]
                if level % 2 == 1:
                    a.reverse()
                ans.append(a)
                new = []
                for i in pre:
                    if i.left:
                        Em = 1
                        new.append(i.left)
                    if i.right:
                        Em = 1
                        new.append(i.right)
                pre = new
                level += 1
        return ans
