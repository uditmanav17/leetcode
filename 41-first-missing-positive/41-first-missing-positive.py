class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for idx, num in enumerate(nums):
            if num <= 0 or num > n:
                nums[idx] = n + 1
        # print(nums)
        
        for idx, num in enumerate(nums):
            num = abs(num)
            if num > n:
                continue
            nums[num-1] = -1 * abs(nums[num-1])
            # print(num, nums)
        
        counts = 0
        for idx, num in enumerate(nums):
            if num > 0:
                return idx + 1
        return n + 1
            
        
            
        