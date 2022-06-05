
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        ans = 0
        any_odd = False
        
        for _, cnt in counts.items():
            q, r = divmod(cnt, 2)
            ans += q * 2
            if r: any_odd = True
                
        return ans + 1 if any_odd else ans
            