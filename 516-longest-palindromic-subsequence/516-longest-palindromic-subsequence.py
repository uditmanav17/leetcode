
# from pprint import pprint as pp

# If the two ends of a string are the same, 
# then they must be included in the longest palindrome subsequence. 
# Otherwise, both ends cannot be included in the longest palindrome subsequence.

class Solution:
    def lps_recursive(self, s, start, end):
        if start == end: return 1
        
        if start > end: return 0  # case like "aa"
        
        if s[start] == s[end]: return 2 + self.lps_recursive(s, start + 1, end - 1)
        
        return max(self.lps_recursive(s, start + 1, end), 
                   self.lps_recursive(s, start, end - 1))
        
        
        
    def lps_memoization(self, s, start, end, memo):
        if start == end: return 1
        
        if start > end: return 0
        
        if memo[start][end] is not None: return memo[start][end]
        
        if s[start] == s[end]:
            memo[start][end] = 2 + self.lps_recursive(s, start + 1, end - 1)
        else:
            memo[start][end] = max( self.lps_recursive(s, start + 1, end), 
                                    self.lps_recursive(s, start, end - 1))

        return memo[start][end]
    
    # then this problems can be reduced to finding the LCS 
    # between the original string and its reversed form
    # check notes for more info
    def lcs(self, x:str):
        y = x[::-1]
        dp = [[0] * (len(x) + 1) for _ in range(len(y) + 1)]

        for i, j in product(range(1, len(y) + 1), range(1, len(x) + 1)):
            # print(y[i - 1], x[j - 1])
            if y[i - 1] == x[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        # pp(dp)
        return dp[-1][-1]

        
    
    def longestPalindromeSubseq(self, s: str) -> int:
        # n = len(s)
        # cache = [[None] * n for _ in range(n)]
        # return self.lps_memoization(s, 0, n - 1, cache)
        
        # return self.lps_recursive(s, 0, n - 1)
        
        return self.lcs(s)
        