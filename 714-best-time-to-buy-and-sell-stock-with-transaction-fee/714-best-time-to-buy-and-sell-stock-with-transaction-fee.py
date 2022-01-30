
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems

# If I am holding a share after today, 
# then either I am just continuing holding the share I had yesterday, 
# or that I held no share yesterday, but bought in one share today: 
#     hold = max(hold, cash - prices[i])

# If I am not holding a share after today, 
# then either I did not hold a share yesterday, 
# or that I held a share yesterday but I decided to sell it out today: 
#     cash = max(cash, hold + prices[i] - fee).
    
# Make sure fee is only incurred once.

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -prices[0]
        
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        
        return cash
