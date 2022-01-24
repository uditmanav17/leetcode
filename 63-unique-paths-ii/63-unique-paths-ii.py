
from itertools import product

class Solution:
    def uniquePathsWithObstacles(self, mat: List[List[int]]) -> int:
        if mat[0][0] == 1:
            return 0
        
        rows = len(mat)
        cols = len(mat[0])

        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = 1

        for r, c in product(range(rows), range(cols)):
            if mat[r][c] == 1:
                continue
                
            if r > 0: 
                dp[r][c] += dp[r-1][c]
            
            if c > 0: 
                dp[r][c] += dp[r][c-1]

        return dp[-1][-1]
