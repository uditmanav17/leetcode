class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = -1
        
        for sub_li in accounts:
            ans = max(ans, sum(sub_li))
            
        return ans
        