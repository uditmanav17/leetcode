from math import factorial

class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        div_factor = 5
        
        while n >= div_factor:
            n, remain = divmod(n, div_factor)
            ans += n
        
        return ans
        