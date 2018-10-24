class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class FuckListnode:
    def __init__(self):
        self.ans = []

    def returnNode(self, a):
        for i in range(len(a)):
            if not self.ans:
                q = ListNode(a[i])
                self.ans.append(q)
            else:
                q = ListNode(a[i])
                self.ans[-1].next = q
                self.ans.append(q)
        return self.ans[0]


if __name__ == '__main__':
    a = [1,2,3,3,4,4,5]
    f = FuckListnode()
    print(f.returnNode(a))