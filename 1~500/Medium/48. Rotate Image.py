from typing import List



class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        matrix.reverse()
        for i in range(n):
            for j in range(i):
                matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]