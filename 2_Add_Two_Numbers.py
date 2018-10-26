# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.numberList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    def addTwoNumbers(self, l1, l2):
        num1 = self.getNode(l1)
        num2 = self.getNode(l2)
        num1.reverse()
        num2.reverse()
        a = self.getnum(num1)
        b = self.getnum(num2)
        res = str(a + b)
        res = res[::-1]
        i = 0
        l = []
        for k in res:
            l.append(ListNode(int(k)))

        while i < len(l) - 1:
            l[i].next = l[i+1]
            i += 1
        return l[0]

    def getNode(self, node):
        lis = [node.val]
        while node.next:
            lis.append(node.next.val)
            node = node.next
        return lis

    def getnum(self, li):
        nun = ''
        for j in li:
            nun += j
        return int(nun)









