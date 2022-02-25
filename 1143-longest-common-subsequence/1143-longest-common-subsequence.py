from pprint import pprint as pp
from itertools import product


class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        l1 = len(t1) + 1
        l2 = len(t2) + 1
        dp = [[0] * l1 for _ in range(l2)]

        for i, j in product(range(1, l2), range(1, l1)):
            # print(i, j)
            ch1, ch2 = t2[i - 1], t1[j - 1]

            if ch1 == ch2:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # pp(dp)

        return dp[-1][-1]

