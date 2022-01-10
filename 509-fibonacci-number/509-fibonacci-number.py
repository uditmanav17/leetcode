class Solution:
    def fib(self, n: int) -> int:
        f0, f1 = 0, 1
        if n <= 1:
            return n
        
        for _ in range(2, n + 1):
            f0, f1 = f1, f0 + f1
            
        return f1
        