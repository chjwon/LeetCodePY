from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        maxSum = len(matrix) - 1 + len(matrix[0]) - 1
        for xySum in range(maxSum+1):
            for x in range(xySum+1):
                if x < len(matrix) and xySum-x < len(matrix[0]):
                    # print([x,xySum-x])
                    if matrix[x][xySum-x] == target:
                        return True
        return False