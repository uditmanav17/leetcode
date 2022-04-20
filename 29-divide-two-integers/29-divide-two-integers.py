class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # print(round(10 / 3), round(7 / -3))
        print(dividend/divisor)
        
        return min(trunc(dividend/divisor), 2147483647)
        