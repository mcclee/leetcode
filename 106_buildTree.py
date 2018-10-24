# Definition for a binary tree node.
class TreeNode:
   def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        root, num1, num2, a, b = self.div(inorder, postorder)
        if root:
            root.left = self.genetree(a, b)
            root.right = self.genetree(num1, num2)
            return root
        else:
            return None

    def genetree(self, ino, poo):
        root, num1, num2, a, b = self.div(ino, poo)
        if root:
            root.left = self.genetree(a, b)
            root.right = self.genetree(num1, num2)
            return root
        else:
            return None
        
    def div(self, num1, num2):
        if num2:
            root = TreeNode(num2.pop())
            lo = num1.index(root.val)
            a, num1 = num1[:lo],  num1[lo+1:]
            b, num2 = num2[:lo], num2[lo:]
            return root, num1, num2, a, b
        else:
            return None, num1, num2, [], []

if __name__ == '__main__':
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    s = Solution()
    a = s.buildTree(inorder, postorder)
    print(a)
    
