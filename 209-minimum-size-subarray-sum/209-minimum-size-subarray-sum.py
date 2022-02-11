class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start_idx = total = 0
        ans = float("inf")
        
        for idx, num in enumerate(nums):
            total += num
            while total >= target:
                ans = min(ans, idx - start_idx + 1)
                total -= nums[start_idx]
                start_idx += 1
                
        return ans if ans != float("inf") else 0