class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ans = [0] * len(cost)
        ans[0] = cost[0]
        ans[1] = cost[1]
        
        for idx in range(2, len(cost)):
            ans[idx] = cost[idx] + min(ans[idx - 1], ans[idx - 2])
            
        # print(ans)
        return min(ans[-2:])