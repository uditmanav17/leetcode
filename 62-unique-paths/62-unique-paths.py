
class Solution:
    def approach1(self, m: int, n: int) -> int:
        return factorial(m + n - 2) // (factorial(m - 1) * factorial(n - 1))
    
    def approach2(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        
        for r, c in product(range(m), range(n)):
            if r==0 or c==0:
                dp[r][c] = 1
                continue
            dp[r][c] = dp[r-1][c] + dp[r][c-1]
            
        return dp[-1][-1]
    
    
    def uniquePaths(self, m: int, n: int) -> int:
        return self.approach2(m, n)
        