from ListToListnode import FuckListnode


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        beg1 = ListNode(0)
        beg2 = ListNode(0)
        pre1 = pre2 = None
        while head:
            if head.val < x:
                if pre1 is None:
                    pre1 = head
                    beg1.next = pre1
                else:
                    pre1.next = head
                    pre1 = pre1.next
            else:
                if pre2 is None:
                    pre2 = head
                    beg2.next = pre2
                else:
                    pre2.next = head
                    pre2 = pre2.next
            head = head.next
        if pre1:
            if pre2:
                pre2.next = None
                pre1.next = beg2.next
            else:
                pre1.next = beg2.next
        else:
            return beg2.next
        return beg1.next


if __name__ == '__main__':
    a = [1,4,3,2,5,2]
    f = FuckListnode()
    q = f.returnNode(a)
    s = Solution()
    print(s.partition(q, 3))
