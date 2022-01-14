# string formatting
# https://colab.research.google.com/github/uditmanav17/CoreySchafer/blob/master/String%20Formatting/String%20Formatting.ipynb

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # check constraints
        n = len(nums)
        nums = set(nums)
        
        max_num = int('1' * n, 2)
        
        while max_num >= 0:
            num = bin(max_num)[2:]
            num = "0" * (n - len(num)) + num
            if num not in nums:
                return num
            max_num -= 1
                
        