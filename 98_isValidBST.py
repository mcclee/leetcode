# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.checknode(root, (float('-inf'), float('inf')))
        return True
            

    def checknode(self, node, bolder):
        if node:
            if self.isv(node, bolder):
                if self.checknode(node.left, (bolder[0], node.val)) and self.checknode(node.right, (node.val, bolder[1])):
                    return True
                else:
                    return False
            else:
                return False
        return True


    def isv(self, node, bolder):
        val = node.val
        if node:
            if bolder[0] >= val:
                    return False
            if bolder[1] <= val:
                    return False
        return True

    
if __name__ == '__main__':
    s = Solution()
    a = TreeNode(0)
    b = TreeNode(-1)
    a.right = b
    print(s.isValidBST(a))
    
