class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for idx, num in enumerate(nums):
            n2 = target - num
            if n2 in seen:
                return [idx, seen[n2]]
            
            seen[num] = idx
            
        
            
        