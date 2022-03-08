class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_ = float("-inf")
        
        for row in accounts:
            max_ = max(max_, sum(row))
            
        return max_
        