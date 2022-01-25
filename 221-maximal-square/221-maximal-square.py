from pprint import pprint as pp

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix) + 1, len(matrix[0]) + 1
        
        dp = [[0] * cols for _ in range(rows)]
        max_edge = 0
        
        for r, c in product(range(1, rows), range(1, cols)):
            if matrix[r-1][c-1] == "1":
                dp[r][c] = 1 + min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1])
                max_edge = max(max_edge, dp[r][c])
                
        # pp(dp)
        return max_edge ** 2
        
        