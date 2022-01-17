
# any pair of consecutive (small, greater) will yield in profit 
# we need to return total profit        

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        for idx in range(1, len(prices)):
            diff = prices[idx] - prices[idx - 1]
            profit += diff if diff > 0 else 0
            
        return profit
        
        