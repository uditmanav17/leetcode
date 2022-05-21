class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans = [float("inf")] * (amount + 1)
        ans[0] = 0
        
        for c in coins:
            for amt in range(amount + 1):
                # print(c, amt)
                if c <= amt:
                    ans[amt] = min(ans[amt - c] + 1, ans[amt])
        
        # print(ans)
        return ans[-1] if ans[-1] != float("inf") else -1
        