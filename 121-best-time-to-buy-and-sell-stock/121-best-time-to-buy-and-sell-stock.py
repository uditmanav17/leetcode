
# find max value, after min arr val

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        prev_min = prices[0]
        
        for ele in prices:
            prev_min = min(prev_min, ele)
            profit = max(profit, ele - prev_min)
            
        return profit

