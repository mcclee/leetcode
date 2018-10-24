class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        lo = {}
        for i in range(len(matrix)):
            if matrix[i][-1] >= target:
                lo = set(matrix[i])
                break
        return target in lo


if __name__ == '__main__':
    a = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]

    s = Solution()
    print(s.searchMatrix(a, 3))