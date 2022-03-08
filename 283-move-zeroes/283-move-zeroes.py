class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swap_idx = 0
        
        for idx, num in enumerate(nums):
            if num != 0:
                nums[swap_idx] = num
                swap_idx += 1
            
        for idx in range(swap_idx, len(nums)):
            nums[idx] = 0
        
        
        