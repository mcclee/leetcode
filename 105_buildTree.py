# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution:

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.goon(preorder, inorder)
    
    def goon(self, preorder, inorder):
        num2, root, inorder = self.findroots(preorder, inorder)
        if root:
            num1 = preorder[1:len(num2) + 1]
            preorder = preorder[len(num2) + 1:]
            root.left = self.goon(num1, num2)
            root.right = self.goon(preorder, inorder)
            return root
        else: 
            return None
            
    def findroots(self, nums1, nums2):
        if nums1:
            root = TreeNode(nums1[0])
            lo = nums2.index(root.val)
            num2 = nums2[:lo]
            nums2 = nums2[lo+1:]
        else:
            num2 = []
            nums2 = []
            root = None
        return num2, root, nums2


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    s = Solution()
    a = s.buildTree(preorder, inorder)
    print(a)
    
'''
class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        stack = [root]
        i, j = 1, 0
        
        while i < len(preorder):
            tmp = None
            node = TreeNode(preorder[i])
            while stack and stack[-1].val == inorder[j]:
                tmp = stack.pop()
                j +=1
            if tmp:
                tmp.right = node
            else:
                stack[-1].left = node
                
            stack.append(node)
            i +=1
        return root
'''