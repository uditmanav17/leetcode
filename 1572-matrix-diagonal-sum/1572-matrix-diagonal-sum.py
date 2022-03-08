class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        
        total = 0
        for r, c in product(range(n), range(n)):
            if (r == c) or ((r + c) == (n - 1)):
                total += mat[r][c]
        
        return total
    