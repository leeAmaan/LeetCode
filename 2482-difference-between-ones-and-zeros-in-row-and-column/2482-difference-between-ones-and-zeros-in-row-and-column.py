class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        m, n = len(grid), len(grid[0])
        row1 = [sum(row) for row in grid]
        col1 = [sum(col) for col in zip(*grid)]
        
        
        for i, row in enumerate(grid):
            for j in range(n):
                row[j] = 2*(row1[i]+col1[j])-m-n
        return grid  
        # ans = [[0 for w in range(n)] for h in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         ans[i][j] = -m -n +2*sum(grid[i]) +2*sum([row[j] for row in grid]) 
        # return ans 
# sum(grid[i]) - (m - sum(grid[i])) + sum(grid[j]) - (n-sum(grid[j]))
