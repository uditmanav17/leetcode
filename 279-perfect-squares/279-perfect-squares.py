from functools import lru_cache
from typing import List
from pprint import pprint as pp


class Solution:
    def numSquares(self, n: int) -> int:
        # return self.recursive_approach(n)
        return self.iterative_approach(n)
        

    def iterative_approach(self, n: int) -> int:
        dp = [float("inf")] * (n+1)
        dp[0] = 0
        
        i = 1
        while i * i <= n:
            square = i * i
            i += 1

            for j in range(square, n+1):
                dp[j] = min(dp[j], dp[j-square] + 1)

        # print(dp)
        return dp[-1]
        
        
    def recursive_approach(self, n: int) -> int:
        
        @lru_cache(None)
        def recurse(n):
            min_val = float("inf")
            if n <= 0:
                return 0

            i = 1
            while i * i <= n:
                ans = 1 + recurse(n - i * i)
                min_val = min(min_val, ans)
                i += 1

            return min_val

        return recurse(n)

