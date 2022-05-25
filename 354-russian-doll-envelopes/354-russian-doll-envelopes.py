class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        envelopes = sorted(envelopes, key = lambda x: (x[0], -x[1]))
        
        dp = [0] * len(envelopes)
        lo, hi = 0, 0
        
        for _, h in envelopes:
            dp[bisect_left(dp, h, lo, hi)] = h
            if dp[hi] == h:
                hi += 1
        
        # print(dp)
        
        return hi
        
        