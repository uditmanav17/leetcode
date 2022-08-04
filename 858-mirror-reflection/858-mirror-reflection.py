class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        GCD = gcd(p, q)
        a = p // GCD; b = q // GCD
        
        if a % 2 == 0:
            return 2

        return 0 if b % 2 == 0 else 1
