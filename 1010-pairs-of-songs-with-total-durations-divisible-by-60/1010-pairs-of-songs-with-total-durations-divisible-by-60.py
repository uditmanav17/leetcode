# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/discuss/1661677/C%2B%2BPythonJava-4-Lines-oror-O(N)-oror-Modulo-and-Count-oror-Detailed-Explanation

# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/discuss/964319/Python-Modular-arithmetic-explained

# there can be several cases how it is possible. Imagine we have 2 songs a and b, then:
# [1]. a and b have reminders 0.
# [2]. a has reminder 1 and b has reminder 59.
# [3]. a has reminder 2 and b has reminder 58.

# [59]. a has reminder 58 and b has reminder 2.
# [60] a has reminder 59 and b has reminder 1.

# So, what we need to do now: for each reminder calculate how many number we have with this reminder and then evaluate sum of products: a1*a59 + a2*a58 + ..., where a1 is number of numbers with reminder 1 and so on. Also we need to be careful with reminders 0 and 30: for them we need to choose number of combinations.

# Complexity: time complexity is O(n), space complexity is O(60) = O(1).

from collections import Counter
from math import comb

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        T = 60
        d = Counter(t % T for t in time)
        
        ans = sum(d[i] * d[T - i] for i in range(1, T // 2))
        
        q1, q2 = d[0], d[T // 2]
        
        return ans + q1 * (q1 - 1) // 2 + q2 * (q2 - 1) // 2
        
        
        