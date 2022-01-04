# N + bitwiseComplement(N) = 11....11 = X
# Then bitwiseComplement(N) = X - N

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        X = 1
        
        while N > X: 
            X = X * 2 + 1
            
        return X - N