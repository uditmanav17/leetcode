class Solution:
    def lcs(self, w1, w2):
        dp = [[0 for _ in range(len(w2) + 1)] for _ in range(len(w1) + 1)]
        
        for idx1, idx2 in product(range(1, len(w1) + 1), range(1, len(w2) + 1)):
            c1 = w1[idx1 - 1]
            c2 = w2[idx2 - 1]
            if c1 == c2:
                dp[idx1][idx2] = dp[idx1-1][idx2-1] + 1
            else:
                dp[idx1][idx2] = max(dp[idx1-1][idx2], dp[idx1][idx2-1])
                    
        # print(dp)
        return dp[-1][-1]
        
    def minDistance(self, word1: str, word2: str) -> int:
        lcs_len = self.lcs(word1, word2)
        return len(word1) + len(word2) - 2 * lcs_len
        
        