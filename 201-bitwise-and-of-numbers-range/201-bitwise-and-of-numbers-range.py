class Solution:
    def rangeBitwiseAnd(self, l: int, r: int) -> int:
        if l == 0 or r == 0 or len(bin(l)) != len(bin(r)):
            return 0
        
        ans = r
        for num in range(l, r):
            ans &= num
            if ans == 0:
                return 0
        
        return ans
    