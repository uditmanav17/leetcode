class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        dp = [[0] * cols for _ in range(rows)]
        
        for r, c in product(range(rows), range(cols)):
            if r == 0 and c == 0:
                dp[r][c] = grid[r][c]
            elif r == 0:
                dp[r][c] = grid[r][c] + dp[r][c-1]
            elif c == 0:
                dp[r][c] = grid[r][c] + dp[r-1][c]
            else:
                dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1])
                
        return dp[-1][-1]
