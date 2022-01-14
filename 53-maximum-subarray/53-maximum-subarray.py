class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane
        curr_max = all_max = nums[0]
        
        for idx in range(1, len(nums)):
            curr_max = max(curr_max + nums[idx], nums[idx])
            all_max = max(all_max, curr_max)
            
        return all_max
            
        
        