class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = float("-inf")
        buy_price = float("inf")
        
        for sell_price in prices:
            buy_price = min(buy_price, sell_price)
            profit = max(profit, sell_price - buy_price)
            
        return profit
                
            