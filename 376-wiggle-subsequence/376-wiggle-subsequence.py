class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up = down = 1
        
        for idx in range(1, len(nums)):
            if nums[idx] < nums[idx - 1]:
                up = down + 1
            elif nums[idx] > nums[idx - 1]:
                down = up + 1
                
        return max(up, down)
                
        
        