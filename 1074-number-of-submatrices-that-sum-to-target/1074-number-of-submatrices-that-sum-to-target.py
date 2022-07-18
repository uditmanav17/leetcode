
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        if not matrix:
            return matrix
        
        rows, cols = len(matrix), len(matrix[0])
        count  = 0
        
        for i in range(rows):
            for j in range(1, cols):
                matrix[i][j] += matrix[i][j-1]
                
                
        sumMap = {}
        for startCol in range(cols):
            for currCol in range(startCol, cols):
                sumMap.clear()
                total = 0
                sumMap[0] = 1
                for row in range(rows):
                    total += matrix[row][currCol] - (matrix[row][startCol-1] if startCol > 0 else 0)
                    count += sumMap.get(total - target, 0)
                    sumMap[total] = sumMap.get(total, 0) + 1
                
        
        return count
        