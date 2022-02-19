class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        
        for r, c in product(range(m), range(n)):
            if r == 0 or c == 0:
                dp[r][c] = 1
            else:
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
                
        # print(dp)
        return dp[-1][-1]
                
        