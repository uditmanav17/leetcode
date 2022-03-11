class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        
        n = len(arr)
        
        for idx, num in enumerate(arr):
            total += ((n-idx)*(idx+1)+1)//2*num
        
        return total
