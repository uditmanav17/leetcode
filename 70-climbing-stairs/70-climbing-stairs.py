
class Solution:
    def __init__(self):
        self.steps = {1:1, 2:2}
        n = 3
        while n <= 45:
            next_steps = self.steps[n-1] + self.steps[n-2]
            self.steps[n] = next_steps
            n += 1
            
    def climbStairs(self, n: int) -> int:
        return self.steps[n]