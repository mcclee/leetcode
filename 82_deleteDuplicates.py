# Definition for singly-linked list.

from ListToListnode import FuckListnode


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        pre, cur = dummy, head
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if pre.next == cur:
                pre = cur
            else:
                pre.next = cur.next
            cur = cur.next
        return dummy.next


if __name__ == '__main__':
    a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 6, 6]
    f = FuckListnode()
    a = f.returnNode(a)
    s = Solution()
    s.deleteDuplicates(a)
