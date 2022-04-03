class Solution:
    
    def reverse_(self, nums, start_idx):
        i = start_idx
        j = len(nums) - 1
        
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = len(nums) - 2
        
        while idx >= 0 and nums[idx + 1] <= nums[idx]:
            idx -= 1
            
        if idx >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[idx]:
                j -= 1
                
            nums[idx], nums[j] = nums[j], nums[idx]
            
        self.reverse_(nums, idx + 1)
        
        