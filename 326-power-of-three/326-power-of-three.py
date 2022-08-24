from math import log

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return ((log10(n) / log10(3)) % 1 == 0) if n > 0 else False
