class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        
        for num in nums:
            if num <= 0 or num > n:
                continue
            
            set_bit = 1 << (num - 1)
            i |= set_bit
            
        ans = bin(i)[2:].zfill(n)
        
        # print(ans)
        for idx, bit in enumerate(ans[::-1], 1):
            if bit == '0':
                return idx
        
        # in case all numbers within array are present
        return idx + 1
        
        