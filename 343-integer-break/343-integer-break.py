
class Solution:
    def integerBreak(self, n: int) -> int:

        d = {1: 1}

        for num in range(2, n + 1):
            d[num] = 0 if num == n else num
            
            for j in range(1, num):
                val = d[j] * d[num - j]
                d[num] = max(d[num], val)
                
        # print(d)
        return d[n]
