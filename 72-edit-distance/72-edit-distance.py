class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        l1, l2 = len(w1) + 1, len(w2) + 1
        
        dp = [[0] * l1 for _ in range(l2)]
        
        for i, j in product(range(l2), range(l1)):
            if i == 0 or j == 0:
                dp[i][j] = i or j
                continue
                
            ch1, ch2 = w1[j - 1], w2[i - 1]
            
            if ch1 == ch2:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                
        return dp[-1][-1]
        