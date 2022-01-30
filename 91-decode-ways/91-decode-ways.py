# https://leetcode.com/problems/decode-ways/discuss/1410879/Python-dp-using-lru_cache-explained

class Solution:
    def numDecodings(self, s: str) -> int:
        
        @lru_cache(None)
        def dp(i):
            if i == -1: return 1
            ans = 0
            
            if s[i] > "0": 
                ans += dp(i-1)
                
            if i >= 1 and "10" <= s[i-1:i+1] <= "26":
                ans += dp(i-2)
            
            return ans
        
        return dp(len(s) - 1)
        