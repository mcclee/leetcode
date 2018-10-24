# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        beg = head
        a = list()
        while beg.next is not None:
            a.append(beg)
            beg = beg.next
        l = len(a)
        k = k % l
        if k != 0:
            a[-1].next = a[0]
            a[l - k - 1].next = None
            return a[l-k]
        else:
            return a[0]


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    s = Solution()
    i = 0
    b = []
    while i < len(a) - 1:
        q = ListNode(a[i])
        q.next = ListNode(a[i + 1])
        b.append(q)
        q = q.next
        i += 1
    b.append(q)

