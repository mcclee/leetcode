from ListToListnode import FuckListnode


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        return self.finddescendants(nodes)

    def finddescendants(self, nodes):
        if nodes:
            div = len(nodes) // 2
            head = TreeNode(nodes[div])
            head.left = self.finddescendants(nodes[:div])
            head.right = self.finddescendants(nodes[div + 1:])
            return head
        else:
            return None


if __name__ == '__main__':
    a = [-10,-3,0,5,9]
    s = Solution()
    f = FuckListnode()
    a = f.returnNode(a)
    ans = s.sortedListToBST(a)
    print(ans)
