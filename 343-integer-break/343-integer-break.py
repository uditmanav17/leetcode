
class Solution:
    def integerBreak(self, n: int) -> int:
        # this should not happen acc to constraint
        if n <= 1:
            return 1
        
        # base cases
        if n <= 3:
            return n - 1
        
        q, r = divmod(n, 3)
        
        # check notes for explanation
        if r == 0:
            return pow(3, q)
        elif r == 1:
            return pow(3, q - 1) * 4
        return pow(3, q) * 2
