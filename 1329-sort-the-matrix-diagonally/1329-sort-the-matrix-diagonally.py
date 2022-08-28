class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diagonals = {}
        rows, cols = len(mat), len(mat[0])
        
        for i, j in product(range(rows), range(cols)):
            diagonals.setdefault(i-j, [])
            diagonals[i-j].append(mat[i][j])
        
        for k in diagonals.keys():
            diagonals[k].sort()
        
        for i, j in product(range(rows), range(cols)):
            mat[i][j] = diagonals[i-j].pop(0)
            
        return mat
