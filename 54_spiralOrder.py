class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        while matrix and matrix[0]:
            ans = ans + matrix[0]
            matrix = matrix[1:]
            if matrix and matrix[0]:
                ans = ans + [x[-1] for x in matrix]
                matrix = [x[: -1] for x in matrix]
            if matrix and matrix[0]:
                ans = ans + matrix[-1][::-1]
                matrix = matrix[:-1]
            if matrix and matrix[0]:
                ans = ans + [x[0] for x in matrix][::-1]
                matrix = [x[1:] for x in matrix]
        return ans


if __name__ == '__main__':
    a = [[ 1, 2, 3 ],[ 8, 9, 4 ],[ 7, 6, 5 ]]
    print(Solution().spiralOrder(a))


