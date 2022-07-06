class Solution:
    def __init__(self):
        self.fibo = {0:0, 1:1}
        for i in range(2, 31):
            self.fibo[i] = self.fibo[i-1] + self.fibo[i-2]
        
    def fib(self, n: int) -> int:
        return self.fibo[n]
        
        