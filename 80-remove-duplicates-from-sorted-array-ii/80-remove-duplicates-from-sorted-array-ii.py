
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        pointer = 1
        for idx in range(2, len(nums)):
            if nums[pointer - 1] != nums[idx]:
                pointer += 1
                nums[pointer] = nums[idx]
                
        return pointer + 1


