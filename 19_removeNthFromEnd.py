# Definition for singly-linked list.
from collections import deque


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next is None and n == 1:
            return None
        elif head.next is None and n != 1:
            return head
        k = head
        nq = deque()
        nq.append(head.val)
        while k.next is not None:
            nq.append(k.next.val)
            k = k.next
        l = len(nq)
        lo = l + 1 - n
        count = 1
        q = ListNode(-1)
        c = q
        while count < lo:
            q.next = head
            q = q.next
            head = head.next
            count += 1
        q.next = head.next
        return c.next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


if __name__ == '__main__':
    a = [1,2]
    p = []
    for i in a:
        if not p:
            j = ListNode(i)
            p.append(j)
        else:
            j = ListNode(i)
            p[-1].next = j
            p.append(j)
    k = p[0]
    s = Solution()
    m = s.removeNthFromEnd(k, 2)
    print(m.val)
    while m.next is not None:
        print(m.next.val)
        m = m.next
