
class Solution:
    def rob_linear(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        ans = [0] * len(nums)
        ans[0] = nums[0]
        ans[1] = max(nums[:2])
        
        for idx in range(2, len(nums)):
            ans[idx] = max(ans[idx - 1], nums[idx] + ans[idx - 2])
            
        return ans[-1]
            
        
    def rob(self, nums: List[int]) -> int:
        # take first, start from 2nd, skip last
        return max(nums[0] + self.rob_linear(nums[2:-1]), 
                   self.rob_linear(nums[1:])) # start from first
        
