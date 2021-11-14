class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        for i in range(1,col):
            grid[0][i] += grid[0][i-1]
        for i in range(1,row):
            grid[i][0] += grid[i-1][0]
        for r in range(1,row):
            for c in range(1,col):
                grid[r][c] += min(grid[r-1][c],grid[r][c-1])
        print(grid)
        return grid[-1][-1]