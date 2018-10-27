from collections import deque
from Fucking_tree import FuckingTree

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        self.getthislevel(deque([root, -1]))

    def getthislevel(self, nums):
        previousnode = nums.popleft()
        currentnode = nums.popleft()
        self.findchildren(previousnode, nums)
        while currentnode != -1:
            previousnode.next = currentnode
            self.findchildren(currentnode, nums)
            previousnode = currentnode
            currentnode = nums.popleft()
        nums.append(-1)
        if nums[0] != -1:
            self.getthislevel(nums)

    def findchildren(self, node, nodelist):
        if node:
            if node.left:
                nodelist.append(node.left)
            if node.right:
                nodelist.append(node.right)


if __name__ == '__main__':
    a = [1,2,3,4,6,7]
    f = FuckingTree(a)
    s = Solution()
    s.connect(f.tree)
    print('Yes')