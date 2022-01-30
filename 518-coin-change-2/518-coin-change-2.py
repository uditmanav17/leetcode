
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = [0] * (amount+1)
        # amount of 0 can be made in only one way
        dp[0] = 1
        
        # iterate over coins
        for coin in coins:
            for amt in range(amount+1):
                # if we have amount >= coins
                # then we add to current possible ways 
                # the number of ways to create (amt-coin)
                if amt >= coin:
                    dp[amt] += dp[amt-coin]
        # print(dp)
        return dp[-1]
