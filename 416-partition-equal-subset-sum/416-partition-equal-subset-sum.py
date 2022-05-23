class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        half_sum, rem = divmod(total, 2)
        if rem:
            return False
        
        @cache
        def is_subset(curr_sum, idx):
            if idx >= len(nums):
                return False
            
            if curr_sum == 0:
                return True
            
            return is_subset(curr_sum - nums[idx], idx + 1) or \
                    is_subset(curr_sum, idx + 1)
        
        return is_subset(half_sum, 0)

