class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # similar to coin change
        dp = [0] * (target+1)
        dp[0] = 1
        
        for idx in range(1, len(dp)):
            for num in nums:
                if idx - num >= 0:
                    dp[idx] += dp[idx-num]
        # print(dp)
        return dp[-1]