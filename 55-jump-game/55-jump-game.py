class Solution:
    def canJump(self, nums: List[int]) -> bool:
        idx = 0
        maxReach = nums[idx]
        n = len(nums)
        
        while idx <= maxReach:
            maxReach = max(maxReach, idx + nums[idx])
            
            # reached last index
            if maxReach >= n - 1:
                return True
            
            idx += 1
            
        return False
                
        