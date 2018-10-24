import copy


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.sum1 = 0
        self.ans = []

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.sum1 = sum
        self.sums(root, 0, [])
        return self.ans

    def sums(self, node, cursum, curlist):
        if node:
            val = node.val
            curlist.append(val)
            cursum += val
            if node.left or node.right:
                self.sums(node.left, cursum, curlist)
                self.sums(node.right, cursum, curlist)
            else:
                if cursum == self.sum1:
                    newlist = copy.deepcopy(curlist)
                    self.ans.append(newlist)
            curlist.pop()
        else:
            return False


if __name__ == '__main__':
    s = Solution()
