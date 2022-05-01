class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        seen = {}
        ans = float("inf")
        
        for idx, ele in enumerate(cards):
            if ele in seen:
                ans = min(ans, idx - seen[ele] + 1)
            seen[ele] = idx
        
        return ans if ans != float("inf") else -1
        