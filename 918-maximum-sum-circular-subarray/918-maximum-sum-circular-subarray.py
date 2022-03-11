class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        # kadane with max/min subarr sum
        
        total = nums[0]
        curr_min = curr_max = all_min = all_max = nums[0]
        
        for idx in range(1, len(nums)):
            curr_max = max(nums[idx], curr_max + nums[idx])
            all_max = max(all_max, curr_max)
            
            curr_min = min(nums[idx], curr_min + nums[idx])
            all_min = min(all_min, curr_min)
            
            total += nums[idx]
            
        # print(all_max, all_min, total)
        
        # corner case - when all nums are -ve OR sum(nums) == all_min
        return max(all_max, total - all_min) if total - all_min > 0 else all_max
    
