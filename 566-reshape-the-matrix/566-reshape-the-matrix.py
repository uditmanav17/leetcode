class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        rows, cols = len(mat), len(mat[0])
        
        if r * c != rows * cols:
            return mat
        
        final_mat = []
        temp_row = []
        
        for cr, cc in product(range(rows), range(cols)):
            temp_row.append(mat[cr][cc])
            
            if len(temp_row) >= c:
                final_mat.append(temp_row[:])
                temp_row.clear()
            
            
        return final_mat
