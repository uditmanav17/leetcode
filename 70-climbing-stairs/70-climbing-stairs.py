
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        
        last = second_last = 1
        
        for idx in range(2, n + 1):
            curr = last + second_last
            second_last, last = last, curr
            
        return curr
            
        
        
        