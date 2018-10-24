from ListToListnode import FuckListnode


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        count = 1
        beg = ListNode(-1)
        beg.next = head
        inter = ListNode(-1)
        rev = []
        while head:
            if m <= count <= n:
                rev.append(head.val)
            if count == m:
                inter.next = head
            if count == n:
                break
            head = head.next
            count += 1
        while rev:
            inter = inter.next
            inter.val = rev.pop()
        return beg.next

        

if __name__ == '__main__':
    a = [1, 2, 3, 4]
    f = FuckListnode()
    q = f.returnNode(a)
    s = Solution()
    print(s.reverseBetween(q, 1, 4))
