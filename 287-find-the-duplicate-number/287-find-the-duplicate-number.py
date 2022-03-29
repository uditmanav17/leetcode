class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        bits = 0
        
        for num in nums:
            curr_bit = 1 << (num - 1)
            if (bits & curr_bit) ^ curr_bit == 0:
                return num
            
            # set bit
            bits ^= curr_bit
        