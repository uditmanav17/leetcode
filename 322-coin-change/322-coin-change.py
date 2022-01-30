class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        coins.sort()
        
        for coin in coins:
            for amt in range(amount+1):
                if amt == coin:
                    dp[amt] = 1
                elif amt > coin:
                    dp[amt] = min(dp[amt-coin] + 1, dp[amt])
        
        # print(dp)
        return dp[-1] if dp[-1] != float("inf") else -1
        
        