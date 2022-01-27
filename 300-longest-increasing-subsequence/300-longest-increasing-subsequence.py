class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lengths = [1] * len(nums)
        
        for idx1 in range(1, len(nums)):
            for idx2 in range(idx1):
                if nums[idx1] > nums[idx2]:
                    lengths[idx1] = max(lengths[idx1], 1 + lengths[idx2])
                    
        # print(lengths)
        return max(lengths)
            
        