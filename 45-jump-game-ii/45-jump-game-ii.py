class Solution:
    def jump(self, nums: List[int]) -> int:
        maxReach = steps = nums[0]
        jump = 0
        
        if steps == 0 or len(nums) == 1:
            return 0
        
        for idx in range(1, len(nums) - 1):
            num = nums[idx]
            maxReach = max(maxReach, idx + num)
            steps -= 1
            
            if steps == 0:
                jump += 1
                steps = maxReach - idx
                
        return jump + 1
