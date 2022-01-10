class Solution:
    def tribonacci(self, n: int) -> int:
        t0, t1, t2 = 0, 1, 1
        if n <= 1:
            return n
        if n == 2:
            return 1
        
        for _ in range(3, n + 1):
            t0, t1, t2 = t1, t2, t0 + t1 + t2
            
        return t2