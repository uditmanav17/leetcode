class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = max_sum = nums[0]
        
        for idx in range(1, len(nums)):
            n = nums[idx]
            curr_sum = max(n, curr_sum + n)
            max_sum = max(max_sum, curr_sum)
            
        return max_sum
        