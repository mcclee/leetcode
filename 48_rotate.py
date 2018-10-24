class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        i = 0
        alll = []
        while i < l:
            j = l-1
            while j >= 0:
                alll.append(matrix[j][i])
                j -= 1
            i += 1
        index = 0
        i = 0
        while i < l:
            matrix.append(alll[index:index + l])
            matrix.pop(0)
            index += l
            i += 1
        print(matrix)


if __name__ == '__main__':
    s = Solution()
    a = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
    s.rotate(a)


