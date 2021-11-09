class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        sol = False
        for i in range(len(matrix)):
            for temp in matrix[i]:
                if temp == target:
                    sol = True
                    break
        return sol