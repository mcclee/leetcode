# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """''
        if head is None:
            return None
        if head.next is None:
            return head
        count = 1
        cur1 = head
        cur2 = cur1.next
        pre = None
        newhead = None
        while cur2.next is not None and cur2.next.next is not None:
            fut = cur2.next
            if pre is not None:
                pre.next = cur2
            cur2.next = cur1
            pre = cur1
            cur1.next = fut
            if count == 1:
                newhead = cur2
            cur1 = fut
            cur2 = cur1.next
            count += 1
        if cur2.next is not None:
            fut = cur2.next
            if pre is not None:
                pre.next = cur2
            cur2.next = cur1
            cur1.next = fut
            if count == 1:
                newhead = cur2
        else:
            if pre is not None:
                pre.next = cur2
            cur2.next = cur1
            cur1.next = None
            if count == 1:
                newhead = cur2
        '''if cur2.next is not None:'''

        return newhead



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


if __name__ == '__main__':
    a = [1,2,3,4,5,6, 7]
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
    m = s.swapPairs(k)
    print(m.val)
    while m.next is not None:
        print(m.next.val)
        m = m.next