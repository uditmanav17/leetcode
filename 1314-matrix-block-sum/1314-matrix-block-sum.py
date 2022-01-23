
class Solution:
    
    def precompute(self, matrix: List[List[int]]):
        # precompute sub matrix sum
        rows = len(matrix) + 1
        cols = len(matrix[0]) + 1
        dp_mat = [[0] * (cols) for _ in range(rows)]

        for r, c in product(range(1, rows), range(1, cols)):
            dp_mat[r][c] = (
                dp_mat[r - 1][c]  # prev_row
                + dp_mat[r][c - 1]  # prev_col
                - dp_mat[r - 1][c - 1]  # prev_row/prev_col
                + matrix[r - 1][c - 1]  # curr matrix element
            )
        self.dp_mat = dp_mat
        
    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return (
            self.dp_mat[r2 + 1][c2 + 1]
            - self.dp_mat[r1][c2 + 1]
            - self.dp_mat[r2 + 1][c1]
            + self.dp_mat[r1][c1]
        )
        
    
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        self.precompute(mat)
        
        rows, cols = len(mat), len(mat[0])
        ans = [[0] * cols for _ in range(rows)]
        
        for r, c in product(range(rows), range(cols)):
            r1 = r - k if (r-k) >= 0 else 0
            c1 = c - k if (c-k) >= 0 else 0
            r2 = r + k if (r+k) < rows else rows-1
            c2 = c + k if (c+k) < cols else cols-1
            
            ans[r][c] = self.sumRegion(r1, c1, r2, c2)
            
        return ans
        
        