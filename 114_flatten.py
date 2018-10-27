from Fucking_tree import FuckingTree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.stack = []

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        org = TreeNode(0)
        org.left = root
        self.checkchild(root)
        self.reshape(root)

    def reshape(self, root):
        if root.left and root.left.val is not None:
            root.right = root.left
            root.left = None
            self.reshape(root.right)

    def checkchild(self, node):
        if node.right and node.right.val is not None:
            self.stack.append(node.right)
            node.right = None
        if node.left and node.left.val is not None:
            node = node.left
            self.checkchild(node)
        else:
            if self.stack:
                node.left = self.stack.pop()
                node = node.left
                self.checkchild(node)
            else:
                return True


if __name__ == '__main__':
    null = None
    a = [1,2,5,3,4,null,6]
    f = FuckingTree(a)
    s = Solution()
    s.flatten(f.tree)
    print('finish')

