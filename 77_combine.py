import copy


class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        c_list = []
        c = []
        self.search(1, c_list, c, n, k)
        return c_list

    def search(self, i, c_list, c, n, k):
        if k == 0:
            c_list.append([x for x in c])
            return

        while i <= n - k + 1:
            c.append(i)
            self.search(i + 1, c_list, c, n, k - 1)
            c.pop()
            i += 1


if __name__ == '__main__':
    s = Solution()
    print(s.combine(5, 4))
