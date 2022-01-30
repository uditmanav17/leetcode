from functools import lru_cache
from typing import List
from pprint import pprint as pp


class Solution:
    def integerBreak(self, n: int) -> int:
        
        @lru_cache(None)
        def break_int(n):
            if n <= 1:
                return 1

            ans = float("-inf")

            for n1 in range(1, n):
                n2 = n - n1
                # print(n, n1, n2)
                a1 = n1 * n2
                a2 = break_int(n1) * break_int(n2)
                a3 = n1 * break_int(n2)
                a4 = break_int(n1) * n2
                ans = max(a1, a2, a3, a4, ans)

            return ans

        return break_int(n)

    