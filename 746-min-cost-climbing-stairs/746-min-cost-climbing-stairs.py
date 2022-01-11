class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ans = [0] * (len(cost))
        ans[0] = cost[0]
        
        for idx in range(1, len(cost)):
            ans[idx] = cost[idx] + min(ans[idx-1], ans[idx-2])
            
        return min(ans[-2:])
        