class Solution:
    def parity_check(self, num):
        return num % 2
    
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x: self.parity_check(x))
        