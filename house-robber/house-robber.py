class Solution:
    def rob(self, nums: List[int]) -> int:
        ans = [0] * len(nums)
        ans[0] = nums[0]
        
        for idx in range(1, len(nums)):
            ans[idx] = max(ans[idx-1], ans[idx-2] + nums[idx])
            
        return ans[-1]
        